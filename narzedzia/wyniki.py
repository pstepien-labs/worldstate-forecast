#!/usr/bin/env python3
"""Liczenie wyników prognoz (metodologia v1.0, §8).

Jedyny skrypt w projekcie. Czyta rejestr CSV (separator ';', UTF-8 z BOM)
i wypisuje wyniki w Markdown.

Użycie:
  python3 narzedzia/wyniki.py                          # wszystkie wydania, wynik na ekran
  python3 narzedzia/wyniki.py --do-wydania 03 --out wydania/.../01_wyniki.md
  python3 narzedzia/wyniki.py --bootstrap A B          # przedział ufności różnicy Briera A−B
"""
import argparse
import csv
import random
from collections import defaultdict
from datetime import date

REJ = 'rejestr/'
PRZEBIEGI = ['A', 'B', 'C', 'AGR', 'AGR_RT']
GRUPY_KIERUNKU = ['USA_ZACHOD', 'UE', 'UKRAINA', 'ROSJA', 'CHINY', 'IRAN', 'KOMPROMIS']


def czytaj(nazwa):
    try:
        with open(REJ + nazwa, encoding='utf-8-sig', newline='') as f:
            return list(csv.DictReader(f, delimiter=';'))
    except FileNotFoundError:
        return []


def d(s):
    return date.fromisoformat(s.strip()[:10])


def rozstrzygniecia_ostateczne(rows):
    """Najwyższa wersja rozstrzygnięcia dla każdego pytania."""
    best = {}
    for r in rows:
        qid = r['id_pytania']
        w = int(r.get('wersja') or 1)
        if qid not in best or w > best[qid][0]:
            best[qid] = (w, r)
    return {k: v[1] for k, v in best.items()}


def srednia(xs):
    return sum(xs) / len(xs) if xs else float('nan')


def fmt(x, n=3):
    return 'b.d.' if x != x else f'{x:.{n}f}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--do-wydania', default=None, help='uwzględnij prognozy do tego wydania włącznie (np. 03)')
    ap.add_argument('--out', default=None)
    ap.add_argument('--bootstrap', nargs=2, metavar=('P1', 'P2'), default=None)
    ap.add_argument('--n-boot', type=int, default=2000)
    a = ap.parse_args()

    pytania = {q['id']: q for q in czytaj('pytania.csv')}
    prognozy = czytaj('prognozy.csv')
    rozs = rozstrzygniecia_ostateczne(czytaj('rozstrzygniecia.csv'))
    bench = czytaj('benchmarki.csv')

    # Rozstrzygnięcia liczone: wynik 0/1; oczekujące na weryfikację osobno.
    wynik, oczekujace, anulowane = {}, [], []
    for qid, r in rozs.items():
        w = r['wynik'].strip().upper()
        if w == 'ANUL':
            anulowane.append(qid)
            continue
        if r.get('weryfikuj', '').strip().upper() == 'T' and r.get('zatwierdzone_przez_uzytkownika', '').strip().upper() != 'T':
            oczekujace.append(qid)
            continue
        if w in ('0', '1'):
            wynik[qid] = int(w)

    wiersze = []  # (qid, wydanie, przebieg, p, o, data)
    for p in prognozy:
        qid = p['id_pytania']
        if qid not in wynik:
            continue
        if a.do_wydania and int(p['wydanie']) > int(a.do_wydania):
            continue
        wiersze.append((qid, p['wydanie'], p['przebieg'], float(p['p']), wynik[qid], p['data']))

    out = []
    pr = out.append
    pr('# Wyniki trafności\n')
    pr(f'Rozstrzygnięte i liczone pytania: **{len(wynik)}** · oczekujące na weryfikację użytkownika: {len(oczekujace)} · anulowane: {len(anulowane)}\n')
    if len(wynik) < 30:
        pr('> Mniej niż 30 rozstrzygniętych pytań — wyniki orientacyjne, bez wniosków o metodzie.\n')

    # Brier wg przebiegu (każda prognoza osobno) i BSS vs status quo na tym samym zbiorze.
    pr('## Przebiegi\n')
    pr('| Przebieg | N prognoz | Brier | Brier SQ (ten sam zbiór) | BSS vs SQ | Brier średnio na pytanie |')
    pr('|---|---|---|---|---|---|')
    for prz in PRZEBIEGI:
        rows = [w for w in wiersze if w[2] == prz]
        if not rows:
            pr(f'| {prz} | 0 | b.d. | b.d. | b.d. | b.d. |')
            continue
        b = [(w[3] - w[4]) ** 2 for w in rows]
        bsq = [(float(pytania[w[0]]['p_status_quo']) - w[4]) ** 2 for w in rows]
        per_q = defaultdict(list)
        for w, x in zip(rows, b):
            per_q[w[0]].append(x)
        bq = srednia([srednia(v) for v in per_q.values()])
        bss = 1 - srednia(b) / srednia(bsq) if srednia(bsq) > 0 else float('nan')
        pr(f'| {prz} | {len(rows)} | {fmt(srednia(b))} | {fmt(srednia(bsq))} | {fmt(bss)} | {fmt(bq)} |')
    pr('')

    oficjalne = [w for w in wiersze if w[2] == 'AGR_RT']

    # Tłum: dopasowania DOKLADNE z tego samego wydania.
    pr('## AGR_RT vs tłum (tylko dopasowania DOKLADNE)\n')
    bmap = defaultdict(list)
    for r in bench:
        if r.get('dopasowanie', '').strip().upper() == 'DOKLADNE':
            bmap[(r['id_pytania'], r['wydanie'])].append(float(r['p']))
    pary = []
    for w in oficjalne:
        key = (w[0], w[1])
        if key in bmap:
            pc = srednia(bmap[key])
            pary.append(((w[3] - w[4]) ** 2, (pc - w[4]) ** 2))
    if pary:
        bm, bc = srednia([x[0] for x in pary]), srednia([x[1] for x in pary])
        bss_c = 1 - bm / bc if bc > 0 else float('nan')
        pr(f'N par: {len(pary)} · Brier AGR_RT: {fmt(bm)} · Brier tłum: {fmt(bc)} · BSS vs tłum: {fmt(bss_c)}\n')
    else:
        pr('Brak rozstrzygniętych pytań z dopasowanym benchmarkiem.\n')

    # Kalibracja AGR_RT.
    pr('## Kalibracja AGR_RT\n')
    pr('| Przedział | N | Średnie p | Częstość TAK |')
    pr('|---|---|---|---|')
    kosze = defaultdict(list)
    for w in oficjalne:
        k = min(int(w[3] * 10), 9)
        kosze[k].append(w)
    for k in range(10):
        ws = kosze.get(k, [])
        pr(f'| {k*10}–{k*10+10}% | {len(ws)} | {fmt(srednia([x[3] for x in ws]), 2)} | {fmt(srednia([x[4] for x in ws]), 2)} |')
    pr('')

    # Błąd kierunkowy.
    pr('## Błąd kierunkowy AGR_RT (średnia p − wynik; neutralnie ≈ 0)\n')
    pr('| czyj_sukces | N | Średni błąd ze znakiem |')
    pr('|---|---|---|')
    for g in GRUPY_KIERUNKU:
        ws = [w for w in oficjalne if pytania[w[0]].get('czyj_sukces', '').strip().upper() == g]
        pr(f'| {g} | {len(ws)} | {fmt(srednia([w[3] - w[4] for w in ws]))} |')
    pr('')

    # Rozbicia: klaster (waga 1 na klaster), wektor, horyzont.
    def rozbicie(tytul, klucz):
        grupy = defaultdict(list)
        for w in oficjalne:
            grupy[klucz(w)].append((w[3] - w[4]) ** 2)
        pr(f'## {tytul}\n')
        pr('| Grupa | N | Brier AGR_RT |')
        pr('|---|---|---|')
        for g in sorted(grupy):
            pr(f'| {g} | {len(grupy[g])} | {fmt(srednia(grupy[g]))} |')
        pr('')
        return grupy

    gk = rozbicie('Klastry', lambda w: pytania[w[0]].get('klaster', '') or 'BRAK')
    pr(f'Brier AGR_RT z wagą 1 na klaster: **{fmt(srednia([srednia(v) for v in gk.values()]))}**\n')
    rozbicie('Wektory', lambda w: pytania[w[0]].get('wektor', ''))

    def horyzont(w):
        try:
            dni = (d(pytania[w[0]]['termin']) - d(w[5])).days
        except Exception:
            return 'nieznany'
        return '≤14 dni' if dni <= 14 else ('≤100 dni' if dni <= 100 else '>100 dni')
    rozbicie('Horyzonty (od daty prognozy do terminu)', horyzont)

    if oczekujace:
        pr('## Oczekujące na weryfikację użytkownika\n')
        pr(', '.join(sorted(oczekujace)) + '\n')

    # Bootstrap po klastrach dla różnicy Briera dwóch przebiegów.
    if a.bootstrap:
        p1, p2 = a.bootstrap
        wsp = defaultdict(dict)
        for w in wiersze:
            if w[2] in (p1, p2):
                wsp[(w[0], w[1])][w[2]] = (w[3] - w[4]) ** 2
        par = [(k[0], v[p1] - v[p2]) for k, v in wsp.items() if p1 in v and p2 in v]
        klastry = defaultdict(list)
        for qid, diff in par:
            klastry[pytania[qid].get('klaster', '') or qid].append(diff)
        klucze = list(klastry)
        random.seed(12345)
        stats = []
        for _ in range(a.n_boot):
            proba = [x for k in (random.choice(klucze) for _ in klucze) for x in klastry[k]]
            stats.append(srednia(proba))
        stats.sort()
        lo, hi = stats[int(0.025 * len(stats))], stats[int(0.975 * len(stats)) - 1]
        pr(f'## Bootstrap: Brier {p1} − Brier {p2}\n')
        pr(f'Par: {len(par)} · klastrów: {len(klucze)} · średnia różnica: {fmt(srednia([x[1] for x in par]))} · 95% PU: [{fmt(lo)}, {fmt(hi)}]')
        pr('Wartość ujemna oznacza, że pierwszy przebieg jest trafniejszy. Przedział obejmujący 0 = brak dowodu różnicy.\n')

    tekst = '\n'.join(out)
    if a.out:
        with open(a.out, 'w', encoding='utf-8') as f:
            f.write(tekst)
    print(tekst)


if __name__ == '__main__':
    main()
