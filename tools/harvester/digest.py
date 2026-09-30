"""Edition digest: turns the local corpus into reading material for stage 02.

Outputs (in editions/<DIR>/02_harvest/ by default):
  G1_digest.md … G4_digest.md  items by concept and day, diverse across countries/languages
  coverage.md                  who spoke about what: languages, countries, W vs non-W,
                               actor-side presence, silent source-universe cells
  indicators.md                latest primary-data values with dates and sources
  sources_health.md            per-source health in the window
  manifest.json                versions, config hashes, window, counts (provenance)

Only titles, short snippets and links go into the edition directory; full
texts stay in data/harvest (not committed).
"""
import glob
import json
import os
import re
from collections import Counter, defaultdict
from datetime import date, timedelta

from . import HARVESTER_VERSION, store
from .config import (ROOT, WESTERN, data_dir, file_hash, iso, load_sources, now, read_csv, read_current,
                     split_list, truthy)

GROUPS = {
    'G1': 'MIL + INF — military, flanks, chokepoints',
    'G2': 'ENE + TEC — energy, raw materials, technology',
    'G3': 'ECO + FIN — trade, sanctions, budgets, central banks, currencies',
    'G4': 'DIP + DOM — diplomacy, alliances, elections, domestic politics, regions',
}
PER_CONCEPT = 40
SNIPPET = 220
CJK = re.compile(r'[぀-ヿ㐀-鿿가-힯]')
# Scripts where words carry attached prefixes or have no spaces: match terms as substrings.
SUBSTRING_SCRIPTS = re.compile('[\u0590-\u05ff\u0600-\u06ff\u0750-\u077f\u3040-\u30ff\u3400-\u9fff\uac00-\ud7af]')


class Matcher:
    """Multilingual concept matcher. All terms are compiled into two alternation
    regexes (word-start terms and substring terms), so matching cost does not
    grow with the number of terms."""

    def __init__(self):
        self.concepts = {}
        self.term_concepts = defaultdict(set)
        word_terms, sub_terms = set(), set()
        for r in read_csv('keywords.csv'):
            c = r['concept']
            meta = self.concepts.setdefault(c, {'label': r.get('label') or c, 'groups': set(), 'pir': r.get('pir', ''),
                                                'actors': set(), 'langs': set()})
            meta['groups'].update(split_list(r.get('groups', ''), ','))
            meta['actors'].update(split_list(r.get('actors', ''), ','))
            meta['langs'].add(r.get('lang', ''))
            if r.get('label') and meta['label'] == c:
                meta['label'] = r['label']
            if r.get('pir') and not meta['pir']:
                meta['pir'] = r['pir']
            for term in split_list(r.get('terms', '')):
                term = term.lower()
                if SUBSTRING_SCRIPTS.search(term):
                    sub_terms.add(term)
                    self.term_concepts[term].add(c)
                else:
                    # prefix match at word start; whole word for terms ending in '$' or of <= 3 characters
                    whole = term.endswith('$') or len(term) <= 3
                    t = term.rstrip('$')
                    word_terms.add((t, whole))
                    self.term_concepts[t].add(c)
        alts = [re.escape(t) + (r'(?!\w)' if whole else '') for t, whole in sorted(word_terms, key=lambda x: -len(x[0]))]
        self.word_re = re.compile(r'(?<!\w)(?:' + '|'.join(alts) + ')') if alts else None
        self.sub_re = re.compile('|'.join(re.escape(t) for t in sorted(sub_terms, key=len, reverse=True))) if sub_terms else None
        # prefix terms can match a longer word start; map the matched text back to its term
        self.prefixes = sorted(self.term_concepts, key=len, reverse=True)

    def _concepts_for(self, matched):
        cs = self.term_concepts.get(matched)
        if cs:
            return cs
        for t in self.prefixes:
            if matched.startswith(t):
                return self.term_concepts[t]
        return set()

    def match(self, text):
        text = text.lower()
        found = set()
        for rx in (self.word_re, self.sub_re):
            if rx is None:
                continue
            for m in rx.finditer(text):
                found |= self._concepts_for(m.group(0))
        return found


def load_items(d_from, d_to):
    items = {}
    d = d_from
    while d <= d_to:
        p = os.path.join(data_dir(), 'items', d.strftime('%Y-%m'), d.isoformat() + '.jsonl')
        if os.path.exists(p):
            with open(p, encoding='utf-8') as f:
                for line in f:
                    try:
                        it = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    items.setdefault(it['id'], it)
        d += timedelta(days=1)
    return list(items.values())


def tokens(title):
    t = title.lower()
    if CJK.search(t):
        t = re.sub(r'\s+', '', t)
        return {t[i:i + 2] for i in range(len(t) - 1)}
    return {w for w in re.findall(r'\w{3,}', t)}


def collapse(items):
    """Merge near-duplicate titles (wire copies, reprints). Token inverted index keeps it fast."""
    groups = []
    index = defaultdict(list)
    for it in items:
        tk = tokens(it['title'])
        best = None
        if tk:
            cand = {}
            for t in tk:
                for gi in index.get(t, ()):
                    cand[gi] = cand.get(gi, 0) + 1
            for gi, shared in sorted(cand.items(), key=lambda x: -x[1])[:20]:
                g = groups[gi]
                if shared / len(tk | g['tk']) >= 0.6:
                    best = g
                    break
        if best is not None:
            best['dups'].append(it)
            continue
        groups.append({'lead': it, 'tk': tk, 'dups': []})
        for t in tk:
            if len(index[t]) < 200:
                index[t].append(len(groups) - 1)
    return groups


ROLE_PRIORITY = {'official': 0, 'state': 1, 'loyal': 1, 'wire': 2, 'independent': 3, 'exile': 3,
                 'western': 4, 'third': 4, 'think_tank': 5, 'data': 5, 'discovered': 6, 'aggregator': 7}


def pick_diverse(groups, n):
    """Round-robin across countries, preferring official/state and larger duplicate groups."""
    by_country = defaultdict(list)
    for g in groups:
        by_country[g['lead'].get('country') or '?'].append(g)
    for lst in by_country.values():
        lst.sort(key=lambda g: (-min(len(g['dups']), 5), ROLE_PRIORITY.get(g['lead'].get('role'), 6)))
    order = sorted(by_country, key=lambda c: -len(by_country[c]))
    out = []
    while len(out) < n and any(by_country.values()):
        for c in order:
            if by_country[c]:
                out.append(by_country[c].pop(0))
                if len(out) >= n:
                    break
    return out


def is_western(country):
    return (country or '').upper() in WESTERN


def fmt_item(g):
    it = g['lead']
    ts = it.get('published') or it.get('fetched') or ''
    t = f"{ts[8:10]}.{ts[5:7]} {ts[11:16]}" if ts else ''
    who = it.get('source_name') or it.get('source_id')
    tag = f"[{it.get('lang') or '?'}·{it.get('country') or '?'}·{it.get('role') or '?'}]"
    dup = ''
    if g['dups']:
        others = sorted({d.get('source_name') or d.get('source_id') for d in g['dups']} - {who})
        dup = f" (+{len(g['dups'])} similar: {', '.join(others[:4])}{'…' if len(others) > 4 else ''})"
    snip = it.get('summary', '')
    snip = (' — ' + snip[:SNIPPET] + ('…' if len(snip) > SNIPPET else '')) if snip and snip[:60] not in it['title'] else ''
    return f"- {t} {tag} **{who}**: {it['title']}{snip} <{it['url']}>{dup}"


def build(d_from, d_to, out_dir, echo=print):
    matcher = Matcher()
    items = load_items(d_from, d_to)
    tasks = {t['id']: t for t in load_sources()}
    echo(f'digest: {len(items)} items in window {d_from}..{d_to}')
    per_concept = defaultdict(list)
    unmatched = 0
    official_unmatched = []
    for it in items:
        cs = matcher.match(it.get('title', '') + ' ' + it.get('summary', ''))
        if not cs:
            unmatched += 1
            if it.get('role') == 'official':
                official_unmatched.append(it)
            continue
        for c in cs:
            per_concept[c].append(it)
    os.makedirs(out_dir, exist_ok=True)

    # ---- group digests ----
    for gid, gname in GROUPS.items():
        concepts = [c for c, m in matcher.concepts.items() if gid in m['groups'] and per_concept.get(c)]
        concepts.sort(key=lambda c: -len(per_concept[c]))
        lines = [f'# Harvest digest {gid} — {gname}', '',
                 f'Window {d_from.strftime("%d.%m.%Y")}–{d_to.strftime("%d.%m.%Y")} · generated {iso(now())} · harvester {HARVESTER_VERSION}', '',
                 'Reading material for stage 02, **not facts**. Every item is a lead: open the link, verify, rate the source, '
                 'decide the perspective (W/A/T) for the specific event, and only then write a fact record. '
                 'Tag `[lang·country·role]`: role comes from the source configuration (`discovered` = found via GDELT; '
                 'country from GDELT metadata). Titles are in the original language.', '']
        if not concepts:
            lines.append('_No items matched the concepts of this group in the window._')
        for c in concepts:
            m = matcher.concepts[c]
            its = per_concept[c]
            langs = Counter(i.get('lang') or '?' for i in its)
            ctry = Counter(i.get('country') or '?' for i in its)
            w = sum(1 for i in its if is_western(i.get('country')))
            actor_hits = sum(1 for i in its if (i.get('country') or '').upper() in {a.upper() for a in m['actors']}
                             or (i.get('actor') or '').upper() in {a.upper() for a in m['actors']})
            lines += [f"## {m['label']} (`{c}`; {m['pir'] or '—'})", '',
                      f"{len(its)} items · {len(langs)} languages ({', '.join(f'{k} {v}' for k, v in langs.most_common(8))}) · "
                      f"{len(ctry)} countries · Western share {round(100 * w / len(its))}% · "
                      f"items from actor countries ({', '.join(sorted(m['actors'])) or '—'}): {actor_hits}", '']
            by_day = Counter((i.get('published') or i.get('fetched'))[:10] for i in its)
            lines.append('Daily volume: ' + ' · '.join(f"{date.fromisoformat(d).strftime('%d.%m')} {n}" for d, n in sorted(by_day.items())))
            lines.append('')
            groups = collapse(sorted(its, key=lambda i: i.get('published') or i.get('fetched') or '', reverse=True))
            chosen = pick_diverse(groups, PER_CONCEPT)
            chosen.sort(key=lambda g: g['lead'].get('published') or g['lead'].get('fetched') or '', reverse=True)
            lines.append(f"Top {len(chosen)} of {len(groups)} distinct stories (diverse by country and language; larger duplicate groups first):")
            lines += [fmt_item(g) for g in chosen]
            if len(groups) > len(chosen):
                lines.append(f'- … more: `python3 -m tools.harvester search {c}` (whole window) or `--day YYYY-MM-DD`')
            lines.append('')
        if gid == 'G4' and official_unmatched:
            lines += ['## Official statements not matched to any concept', '']
            groups = collapse(sorted(official_unmatched, key=lambda i: i.get('published') or '', reverse=True))
            lines += [fmt_item(g) for g in groups[:60]]
        store.write_atomic(os.path.join(out_dir, f'{gid}_digest.md'), '\n'.join(lines) + '\n')

    # ---- coverage ----
    cov = coverage(items, per_concept, matcher, tasks, d_from, d_to, unmatched)
    store.write_atomic(os.path.join(out_dir, 'coverage.md'), cov['md'])
    # ---- indicators ----
    store.write_atomic(os.path.join(out_dir, 'indicators.md'), indicators_md(d_from, d_to, tasks))
    # ---- health ----
    store.write_atomic(os.path.join(out_dir, 'sources_health.md'), health_md(tasks))
    manifest = {
        'harvester_version': HARVESTER_VERSION,
        'framework_version': _read(os.path.join(ROOT, 'VERSION')).strip(),
        'generated': iso(now()), 'window': [d_from.isoformat(), d_to.isoformat()],
        'config_hashes': {n: file_hash(n) for n in ('feeds.csv', 'datasets.csv', 'keywords.csv', 'countries.csv', 'sites.csv', 'forbidden_domains.txt')},
        'items_in_window': len(items), 'items_matched': len(items) - unmatched,
        'concepts': {c: len(v) for c, v in sorted(per_concept.items())},
        'languages': dict(Counter(i.get('lang') or '?' for i in items).most_common()),
        'countries': len({i.get('country') for i in items if i.get('country')}),
        'western_share_pct': round(100 * sum(1 for i in items if is_western(i.get('country'))) / max(1, len(items)), 1),
        'sources_enabled': sum(1 for t in tasks.values() if truthy(t.get('enabled', '1'))),
        'sources_with_items_in_window': len({i['source_id'] for i in items}),
        'silent_universe_cells': cov['silent'],
    }
    store.write_atomic(os.path.join(out_dir, 'manifest.json'), json.dumps(manifest, ensure_ascii=False, indent=1))
    echo(f'digest written to {out_dir}')
    return manifest


def _read(p):
    try:
        with open(p, encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ''


def coverage(items, per_concept, matcher, tasks, d_from, d_to, unmatched):
    lines = ['# Harvest coverage', '', f'Window {d_from.strftime("%d.%m.%Y")}–{d_to.strftime("%d.%m.%Y")} · generated {iso(now())}', '']
    langs = Counter(i.get('lang') or '?' for i in items)
    ctry = Counter(i.get('country') or '?' for i in items)
    w = sum(1 for i in items if is_western(i.get('country')))
    lines += ['## Totals', '',
              f'- Items in window: {len(items)}; matched to at least one concept: {len(items) - unmatched}',
              f'- Languages: {len(langs)} — ' + ', '.join(f'{k} {v}' for k, v in langs.most_common(20)),
              f'- Countries of publication: {len(ctry)} — top: ' + ', '.join(f'{k} {v}' for k, v in ctry.most_common(15)),
              f'- Western share of items: {round(100 * w / max(1, len(items)))}%', '']
    # concept balance
    lines += ['## Perspective balance by concept', '',
              'W = publication country in the Western set; "actor" = items from the countries listed as actors for the concept. '
              'Flags: ⚠W>80% (Western-dominated), ⚠no actor (no items from actor countries), ⚠<3 lang.', '',
              '| Concept | Items | Languages | Countries | W % | Actor-country items | Flags |', '|---|---|---|---|---|---|---|']
    for c, m in sorted(matcher.concepts.items(), key=lambda x: -len(per_concept.get(x[0], []))):
        its = per_concept.get(c, [])
        if not its:
            lines.append(f"| {m['label']} | 0 | 0 | 0 | — | 0 | ⚠ silent |")
            continue
        wl = sum(1 for i in its if is_western(i.get('country')))
        actors = {a.upper() for a in m['actors']}
        ah = sum(1 for i in its if (i.get('country') or '').upper() in actors or (i.get('actor') or '').upper() in actors)
        nl = len({i.get('lang') for i in its})
        flags = []
        if 100 * wl / len(its) > 80:
            flags.append('⚠W>80%')
        if actors and ah == 0:
            flags.append('⚠no actor')
        if nl < 3:
            flags.append('⚠<3 lang')
        lines.append(f"| {m['label']} | {len(its)} | {nl} | {len({i.get('country') for i in its})} | "
                     f"{round(100 * wl / len(its))} | {ah} | {' '.join(flags) or 'ok'} |")
    # source universe
    uni = read_csv('source_universe.csv')
    silent = []
    if uni:
        roles = ['official', 'state_loyal', 'independent_exile', 'western', 'third']
        role_map = {'official': 'official', 'state': 'state_loyal', 'loyal': 'state_loyal', 'independent': 'independent_exile',
                    'exile': 'independent_exile', 'western': 'western', 'wire': 'western', 'third': 'third', 'think_tank': 'independent_exile'}
        cnt = defaultdict(int)
        feeds_cnt = defaultdict(int)
        for i in items:
            r = role_map.get(i.get('role'))
            if r and i.get('actor'):
                cnt[(i['actor'].upper(), r)] += 1
        for t in tasks.values():
            r = role_map.get(t.get('role'))
            if r and t.get('actor') and truthy(t.get('enabled', '1')):
                feeds_cnt[(t['actor'].upper(), r)] += 1
        lines += ['', '## Source universe: configured sources and items per actor and role', '',
                  'Cell = items in window (configured sources). Required roles per actor come from `sources/harvest/source_universe.csv`. '
                  '⚠ = required role with no items.', '',
                  '| Actor | Priority | ' + ' | '.join(roles) + ' |', '|---|---|' + '---|' * len(roles)]
        for u in uni:
            a = u['actor'].upper()
            req = set(split_list(u.get('required_roles', ''), ','))
            cells = []
            for r in roles:
                n, f = cnt.get((a, r), 0), feeds_cnt.get((a, r), 0)
                mark = ''
                if r in req and n == 0:
                    mark = ' ⚠'
                    silent.append(f'{a}:{r}')
                cells.append(f'{n} ({f}){mark}' if (f or r in req) else '·')
            lines.append(f"| {u.get('name', a)} ({a}) | {u.get('priority', '')} | " + ' | '.join(cells) + ' |')
        lines += ['', f'Silent required cells: {len(silent)} — ' + (', '.join(silent) if silent else 'none'), '',
                  'Stage 02 must close silent cells for key events with targeted web search, or record them as gaps (section J).']
    return {'md': '\n'.join(lines) + '\n', 'silent': silent}


def load_observations():
    p = os.path.join(data_dir(), 'datasets', 'observations.jsonl')
    out = defaultdict(list)
    if os.path.exists(p):
        with open(p, encoding='utf-8') as f:
            for line in f:
                try:
                    o = json.loads(line)
                except json.JSONDecodeError:
                    continue
                out[(o['source_id'], o['indicator'])].append(o)
    return out


def indicators_md(d_from, d_to, tasks):
    obs = load_observations()
    lines = ['# Primary-data indicators', '',
             f'Harvested directly from primary sources. Window {d_from.strftime("%d.%m.%Y")}–{d_to.strftime("%d.%m.%Y")}. '
             'Use these values (with the dataset URL as the source) in fact records and block L instead of second-hand reports. '
             'A value dated after the state date must not be used as the state value.', '',
             '| Indicator | Latest in window | Date | Previous | Change | Obs in window | Source |', '|---|---|---|---|---|---|---|']
    for (sid, ind), rows in sorted(obs.items()):
        rows = sorted({r['date']: r for r in rows}.values(), key=lambda r: r['date'])
        win = [r for r in rows if d_from.isoformat() <= r['date'] <= d_to.isoformat()]
        if not win:
            continue
        last = win[-1]
        prev = win[-2] if len(win) > 1 else None
        ch = f"{last['value'] - prev['value']:+.4g}" if prev else '—'
        t = tasks.get(sid, {})
        lines.append(f"| {ind} | {last['value']:.6g} {last.get('unit', '')} | {last['date']} | "
                     f"{(str(round(prev['value'], 6)) + ' (' + prev['date'] + ')') if prev else '—'} | {ch} | {len(win)} | "
                     f"{t.get('name', sid)} |")
    raw_dir = os.path.join(data_dir(), 'datasets', 'raw')
    snaps = []
    for t in tasks.values():
        if t.get('kind') == 'dataset' and t.get('adapter') == 'snapshot':
            files = sorted(glob.glob(os.path.join(raw_dir, t['id'], '*')))
            if files:
                snaps.append(f"- {t.get('name')}: latest snapshot `{os.path.relpath(files[-1], ROOT)}`")
    if snaps:
        lines += ['', '## Raw snapshots (read locally)', ''] + snaps
    return '\n'.join(lines) + '\n'


def health_md(tasks):
    state = store.read_json(os.path.join(data_dir(), 'state', 'sources.json'), {})
    lines = ['# Source health', '', f'Generated {iso(now())}', '',
             '| Source | Kind | Lang | Actor | Role | Status | Items total | Last success | Last error |', '|---|---|---|---|---|---|---|---|---|']
    for sid, t in sorted(tasks.items()):
        if not truthy(t.get('enabled', '1')):
            continue
        e = state.get(sid, {})
        lines.append(f"| {sid} | {t.get('kind')}{'/' + t['adapter'] if t.get('adapter') else ''} | {t.get('lang', '')} | "
                     f"{t.get('actor', '')} | {t.get('role', '')} | {e.get('status', 'never_run')} | "
                     f"{e.get('items_total', e.get('obs_total', 0))} | {e.get('last_success') or '—'} | {(e.get('last_error') or '')[:80]} |")
    return '\n'.join(lines) + '\n'


def default_window():
    cur = read_current()
    d_from = date.fromisoformat(cur['PERIOD_FROM']) if cur.get('PERIOD_FROM') else date.today() - timedelta(days=14)
    d_to = date.fromisoformat(cur['STATE_DATE']) if cur.get('STATE_DATE') else date.today()
    out = os.path.join(ROOT, cur['DIRECTORY'], '02_harvest') if cur.get('DIRECTORY') else os.path.join(data_dir(), 'digest')
    return d_from, d_to, out


def search(concept_or_text, day=None, limit=200, d_from=None, d_to=None):
    matcher = Matcher()
    if day:
        d = date.fromisoformat(day)
        items = load_items(d, d)
    else:
        w_from, w_to, _ = default_window()
        items = load_items(date.fromisoformat(d_from) if d_from else w_from, date.fromisoformat(d_to) if d_to else w_to)
    out = []
    for it in items:
        text = it.get('title', '') + ' ' + it.get('summary', '')
        if concept_or_text in matcher.concepts:
            if concept_or_text in matcher.match(text):
                out.append(it)
        elif concept_or_text.lower() in text.lower():
            out.append(it)
    out.sort(key=lambda i: i.get('published') or '', reverse=True)
    return out[:limit]
