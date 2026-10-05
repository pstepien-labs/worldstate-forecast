"""Offline end-to-end test: a local HTTP server with fake feeds, a Telegram
preview, a GDELT-like answer is not used (external API), datasets (NBP, SDMX,
FRED), a watched page; a simulated crash in the middle of a sweep; resume;
digest. Uses a temporary data and config directory — your real data is not touched.
"""
import http.server
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
from datetime import datetime, timedelta, timezone

NOW = datetime.now(timezone.utc)
D1 = (NOW - timedelta(days=1)).strftime('%a, %d %b %Y 10:00:00 +0000')
D2 = (NOW - timedelta(days=2)).strftime('%Y-%m-%dT09:30:00Z')
DAY = (NOW - timedelta(days=1)).strftime('%Y-%m-%d')

FILES = {
    'robots.txt': 'User-agent: *\nDisallow: /private/\n',
    'rss.xml': f'''<?xml version="1.0"?><rss version="2.0"><channel><title>T</title>
<item><title>Tankers attacked near the Strait of Hormuz</title><link>http://HOST/a1?utm_source=x</link><description>Two tankers hit &amp; damaged</description><pubDate>{D1}</pubDate></item>
<item><title>Central bank keeps interest rate unchanged</title><link>http://HOST/a2</link><description>Rates</description><pubDate>{D1}</pubDate></item>
<item><title>Broken & unescaped ampersand story about sanctions</title><link>http://HOST/a3</link><pubDate>{D1}</pubDate></item>
</channel></rss>''',
    'atom.xml': f'''<?xml version="1.0" encoding="utf-8"?><feed xmlns="http://www.w3.org/2005/Atom"><title>A</title>
<entry><title>Ормузский пролив: танкеры атакованы</title><link href="http://HOST/r1"/><updated>{D2}</updated><summary>Иран</summary></entry>
<entry><title>Duplicate of first RSS item</title><link href="http://HOST/a1"/><updated>{D2}</updated></entry>
</feed>''',
    'tg.html': f'''<html><div class="tgme_widget_message_wrap js-widget_message_wrap"><div data-post="chan/101">
<div class="tgme_widget_message_text js-message_text" dir="auto">Drone attack on the refinery, fire reported<br/>more text</div>
<time datetime="{D2}">t</time></div></div></html>''',
    'page.html': '<html><body><p>Press conference of the Ministry of Foreign Affairs, statement one about sanctions.</p></body></html>',
    'page2.html': '<html><body><p>Press conference of the Ministry of Foreign Affairs, statement one about sanctions.</p><p>New statement: firm opposition to the new tariffs and export controls.</p></body></html>',
    'nbp.json': json.dumps({'rates': [{'effectiveDate': DAY, 'mid': 4.2512}]}),
    'sdmx.csv': f'KEY,TIME_PERIOD,OBS_VALUE\nX,{DAY},1.1734\n',
    'fred.csv': f'observation_date,DCOILBRENTEU\n{DAY},99.25\n',
    'private/x.xml': 'blocked by robots',
}

FEEDS = '''id;enabled;kind;name;url;lang;country;actor;role;tier;groups;interval_h;notes
t_rss;1;rss;Test RSS;http://HOST/rss.xml;en;GB;GB;western;B;G1|G3;6;
t_atom;1;rss;Test Atom;http://HOST/atom.xml;ru;RU;RU;state;C;G1;6;
t_tg;1;telegram;Test TG;http://HOST/tg.html;ru;RU;RU;loyal;D;G1;6;
t_page;1;page;Test MFA page;http://HOST/page.html;en;CN;CN;official;B;G4;12;
t_robots;1;rss;Robots-blocked;http://HOST/private/x.xml;en;US;US;western;B;G1;6;
t_dead;1;rss;Dead feed;http://HOST/missing.xml;en;US;US;western;B;G1;6;
t_429;1;rss;Rate-limited feed;http://LOCALHOST/ratelimit.xml;en;US;US;western;B;G1;6;
'''
DATASETS = '''id;enabled;adapter;name;url;params;indicator;unit;needs_key;interval_h;groups;notes
d_nbp;1;nbp;NBP EUR/PLN;http://HOST/nbp.json;;EUR/PLN;PLN;;24;G3;
d_sdmx;1;sdmx_csv;ECB EUR/USD;http://HOST/sdmx.csv;;EUR/USD;USD;;24;G3;
d_fred;1;fred_csv;FRED Brent;http://HOST/fred.csv;;Brent;USD/bbl;;24;G2;
d_key;1;eia;Needs key;http://HOST/x?k={key:SELFTEST_MISSING_KEY};;X;;SELFTEST_MISSING_KEY;24;G2;
'''
KEYWORDS = '''concept;label;groups;vectors;pir;actors;lang;terms
hormuz;Strait of Hormuz;G1,G2;INF;PIR-5;IR;en;hormuz|tanker
hormuz;Strait of Hormuz;G1,G2;INF;PIR-5;IR;ru;ормузск|танкер
rates;Central banks;G3;FIN;PIR-6;;en;interest rate|central bank
sanctions;Sanctions;G3;FIN;PIR-6;RU;en;sanction|export control|tariff
drones;Drones;G1;MIL;PIR-1;RU,UA;en;drone
'''
UNIVERSE = '''actor;name;priority;required_roles
RU;Russia;1;official,state_loyal,independent_exile
CN;China;1;official,state_loyal
'''


class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        if self.path.startswith('/ratelimit'):
            self.send_response(429)
            self.send_header('Retry-After', '120')
            self.end_headers()
            return
        return super().do_GET()


def main():
    tmp = tempfile.mkdtemp(prefix='harvest-selftest-')
    web = os.path.join(tmp, 'web')
    cfg = os.path.join(tmp, 'config')
    data = os.path.join(tmp, 'data')
    os.makedirs(os.path.join(web, 'private'))
    os.makedirs(cfg)
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), lambda *a, **k: Handler(*a, directory=web, **k))
    host = f'127.0.0.1:{srv.server_address[1]}'
    for name, body in FILES.items():
        with open(os.path.join(web, name), 'w', encoding='utf-8') as f:
            f.write(body.replace('HOST', host))
    for name, body in {'feeds.csv': FEEDS, 'datasets.csv': DATASETS, 'keywords.csv': KEYWORDS,
                       'source_universe.csv': UNIVERSE, 'forbidden_domains.txt': 'polymarket.com\n',
                       'countries.csv': 'code;names\nGB;United Kingdom\n', 'sites.csv': 'id;name;lat;lon;radius_km\n'}.items():
        with open(os.path.join(cfg, name), 'w', encoding='utf-8') as f:
            f.write(body.replace('LOCALHOST', 'localhost:' + host.split(':')[1]).replace('HOST', host))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    env = dict(os.environ, HARVEST_DATA=data, HARVEST_CONFIG=cfg, HARVEST_MIN_DELAY='0', HARVEST_BACKFILL_DAYS='5',
               NO_PROXY='127.0.0.1,localhost', no_proxy='127.0.0.1,localhost')
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

    def hv(*args, extra=None):
        e = dict(env, **(extra or {}))
        return subprocess.run([sys.executable, '-m', 'tools.harvester', *args], cwd=root, env=e,
                              capture_output=True, text=True, timeout=120)

    checks = []

    def ok(name, cond, detail=''):
        checks.append((name, bool(cond), detail))

    # 1) crash after 3 sources
    r = hv('run', extra={'HARVEST_TEST_CRASH_AFTER': '3'})
    ok('simulated crash exits non-zero', r.returncode == 3, f'rc={r.returncode}')
    state = json.load(open(os.path.join(data, 'state', 'sources.json')))
    done_first = [k for k, v in state.items() if v.get('status')]
    first_attempts = {k: state[k]['last_attempt'] for k in done_first}
    ok('checkpoint written for sources done before crash', len(done_first) == 3, str(done_first))
    # 2) resume: lock from dead pid must be taken over, remaining sources run, done ones skipped
    r = hv('run')
    ok('resume run succeeds', r.returncode == 0, r.stderr[-300:])
    ok('stale lock taken over', 'stale_lock_removed' in r.stdout)
    state = json.load(open(os.path.join(data, 'state', 'sources.json')))
    ok('all sources attempted after resume', len(state) == 11, str(sorted(state)))
    ok('sources done before crash not refetched', all(state[k]['last_attempt'] == first_attempts[k] for k in done_first))
    ok('robots.txt respected', state['t_robots'].get('status') == 'skipped', state['t_robots'].get('last_error'))
    ok('dead feed backs off', state['t_dead'].get('status') == 'retrying', state['t_dead'].get('last_error'))
    ok('rate limit (429) pauses the host, not counted as failure',
       state['t_429'].get('status') == 'throttled' and not state['t_429'].get('consecutive_failures'), str(state['t_429']))
    ok('missing API key skipped, not failed', state['d_key'].get('status') == 'skipped', state['d_key'].get('last_error'))
    # 3) nothing due now
    r = hv('run')
    ok('second run finds nothing due', 'due=0' in r.stdout, r.stdout[-200:])
    # 4) page change detection
    shutil.copy(os.path.join(web, 'page2.html'), os.path.join(web, 'page.html'))
    r = hv('check', '--only', 't_page')
    items = []
    for dp, _, fs in os.walk(os.path.join(data, 'items')):
        for fn in fs:
            items += [json.loads(line) for line in open(os.path.join(dp, fn), encoding='utf-8')]
    ids = [i['id'] for i in items]
    ok('deduplication across feeds (utm stripped)', len(ids) == len(set(ids)) and
       sum(1 for i in items if i['url'].split('?')[0].endswith('/a1')) == 1, str(len(items)))
    ok('broken XML parsed', any('ampersand' in i['title'] for i in items))
    ok('telegram parsed', any(i['source_id'] == 't_tg' for i in items))
    ok('page change detected', any(i['source_id'] == 't_page' and 'firm opposition' in i['summary'] for i in items))
    obs = [json.loads(line) for line in open(os.path.join(data, 'datasets', 'observations.jsonl'))]
    ok('datasets parsed (NBP, SDMX, FRED)', {o['source_id'] for o in obs} == {'d_nbp', 'd_sdmx', 'd_fred'}, str(obs))
    # 5) status + digest
    r = hv('status')
    ok('status renders', 'Harvester status' in r.stdout and 'LIVENESS' in r.stdout)
    out = os.path.join(tmp, 'digest')
    r = hv('digest', '--from', (NOW - timedelta(days=5)).strftime('%Y-%m-%d'), '--to', NOW.strftime('%Y-%m-%d'), '--out', out)
    ok('digest builds', r.returncode == 0, r.stderr[-300:])
    g1 = open(os.path.join(out, 'G1_digest.md'), encoding='utf-8').read() if os.path.exists(os.path.join(out, 'G1_digest.md')) else ''
    ok('digest groups multilingual items under one concept', 'Ормузский' in g1 and 'Hormuz' in g1)
    cov = open(os.path.join(out, 'coverage.md'), encoding='utf-8').read() if os.path.exists(os.path.join(out, 'coverage.md')) else ''
    ok('coverage flags silent universe cells', 'Silent required cells' in cov)
    ind = open(os.path.join(out, 'indicators.md'), encoding='utf-8').read() if os.path.exists(os.path.join(out, 'indicators.md')) else ''
    ok('indicators table has values', '99.25' in ind and '4.2512' in ind)
    srv.shutdown()
    width = max(len(c[0]) for c in checks)
    failed = 0
    for name, passed, detail in checks:
        print(f"{'PASS' if passed else 'FAIL'}  {name.ljust(width)}  {'' if passed else detail}")
        failed += not passed
    print(f'\n{len(checks) - failed}/{len(checks)} checks passed. Temporary files: {tmp}')
    if not failed:
        shutil.rmtree(tmp, ignore_errors=True)
    return 1 if failed else 0
