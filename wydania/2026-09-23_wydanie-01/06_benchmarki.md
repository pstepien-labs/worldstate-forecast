# Etap 06 — Benchmarki (wydanie 01, stan 23.09.2026)

Benchmarki zebrano **po** commicie „wydanie-01 prognozy zamrożone” (32a635e). Materiał służy do przeglądu. **Nie** jest podstawą do zmiany prognoz: żadnej prognozy nie zmieniono. Do raportu głównego nie wchodzi (metodologia §6); do `07_zalacznik_benchmarki.md`.

## 1. Źródła i dostęp

| Źródło | Dostęp | Wynik |
|---|---|---|
| Polymarket | Strona zwraca ECONNREFUSED dla narzędzia WebFetch; notowania pobrano z publicznego API tylko do odczytu (gamma-api.polymarket.com) | 25 wierszy |
| Kalshi | Publiczne API tylko do odczytu (api.elections.kalshi.com) | 13 wierszy |
| Manifold | Publiczne API wyszukiwania (api.manifold.markets) | 9 wierszy (waluta gry, zwykle niska płynność) |
| Good Judgment Open | Strony publiczne (bez logowania) | 2 wiersze; wiele pytań GJO nie pasuje do banku |
| Metaculus | API wymaga konta, a strony pytań zwracają HTTP 403. Nie logowano się (CLAUDE.md §6) | 0 wierszy; znaleziono m.in. pytanie 43318 „general mobilization before 01.01.2027”, ale bez wartości |
| RAND Forecasting Initiative | Platforma zamknięta, dostępne tylko archiwum rozstrzygniętych pytań | 0 wierszy |

Konwencja zapisu: p = środek widełek bid/ask (Polymarket: `outcomePrices`, czyli środek; Kalshi: (bid+ask)/2). Wartości spoza zakresu 0.01–0.99 przycięto do tego zakresu, a surowe notowanie podano w polu `uwagi`. Data notowań: 23.09.2026, wieczór (czas PL). Zapis w `rejestr/benchmarki.csv`: 43 wiersze, 26 pytań; 20 wierszy DOKLADNE dla 12 pytań.

## 2. Dopasowania

Kolumna AGR_RT to oficjalna prognoza zamrożona. Δ = tłum − AGR_RT.

| ID | Pytanie (skrót) | AGR_RT | Źródło | p tłumu | Dopasowanie | Δ |
|---|---|---|---|---|---|---|
| Q-0001 | Dekret o mobilizacji RU do 31.12 | 0.030 | Polymarket | 0.26 | PRZYBLIZONE | **+0.23** |
| Q-0001 | | | Manifold | 0.27 | DOKLADNE | **+0.24** |
| Q-0006 | Brent > 100 USD 06.10 | 0.400 | Kalshi (30.09) | 0.42 | DOKLADNE | +0.02 |
| Q-0011 | Przedłużenie rozejmu USA–ChRL do 10.11 | 0.750 | Kalshi (do 01.11) | 0.505 | PRZYBLIZONE | **−0.25** |
| Q-0011 | | | Polymarket (do 31.10) | 0.835 | PRZYBLIZONE | +0.09 |
| Q-0016 | RPP zmienia stopę do 31.12 | 0.183 | Kalshi (tylko X) | 0.075 | PRZYBLIZONE | −0.11 |
| Q-0017 | EBC podnosi stopę X–XII | 0.433 | Polymarket (XII) | 0.64 | PRZYBLIZONE | **+0.21** |
| Q-0018 | Bank z ChRL na SDN do 31.03.2027 | 0.087 | Kalshi (do 01.01.2027) | 0.315 | PRZYBLIZONE | **+0.23** |
| Q-0020 | Bank Rosji obniża stopę 23.10 | 0.250 | Polymarket | 0.275 | DOKLADNE | +0.03 |
| Q-0026 | Spotkanie trójstronne USA–UA–RU do 30.11 | 0.450 | Kalshi (przywódcy, do 01.01) | 0.035 | PRZYBLIZONE | **−0.42** |
| Q-0026 | | | Polymarket (RU–UA, do 31.10) | 0.645 | PRZYBLIZONE | +0.195 (poniżej progu) |
| Q-0027 | Wniosek z art. 4 NATO do 31.12 | 0.113 | Polymarket | 0.47 | DOKLADNE | **+0.36** |
| Q-0030 | Spotkanie Putin–Trump do 31.03.2027 | 0.267 | Polymarket (do 31.12) | 0.765 | PRZYBLIZONE | **+0.50** |
| Q-0030 | | | Manifold (2026) | 0.274 | PRZYBLIZONE | +0.01 |
| Q-0031 | Republikanie ≥ 218 mandatów | 0.107 | Polymarket / Kalshi / Manifold | 0.075 / 0.082 / 0.062 | DOKLADNE | −0.03 / −0.03 / −0.05 |
| Q-0032 | Nowe nagranie Modżtaby Chameneiego | 0.140 | Polymarket (foto/wideo) | 0.195 | PRZYBLIZONE | +0.06 |
| Q-0033 | Lula wygrywa wybory | 0.557 | Polymarket / Kalshi / Manifold / GJO | 0.405 / 0.435 / 0.373 / 0.50 | DOKLADNE | −0.15 / −0.12 / −0.18 / −0.06 |
| Q-0034 | Wenezuela: data wyborów do 31.03.2027 | 0.333 | Polymarket | 0.165 | PRZYBLIZONE | −0.17 |
| Q-0035 | Goïta traci władzę do 31.03.2027 | 0.093 | Polymarket (do 31.12) | 0.075 | PRZYBLIZONE | −0.02 |
| Q-0036 | Ormuz: średnia 7-dniowa > 40 do 31.12 | 0.240 | Kalshi | 0.18 | DOKLADNE | −0.06 |
| Q-0036 | | | Polymarket (≥ 60) / GJO (≥ 35, do 11.01) | 0.205 / 0.333 | PRZYBLIZONE | −0.04 / +0.09 |
| Q-0037 | Ormuz: ≥ 20 przejść w dobie do 07.10 | 0.113 | Polymarket (do 30.09) | 0.041 | DOKLADNE | −0.07 |
| Q-0037 | | | Kalshi (wrzesień) | 0.045 | PRZYBLIZONE | −0.07 |
| Q-0041 | Uderzenie USA na Iran do 07.10 | 0.060 | Polymarket (zerwanie rozejmu do 30.09) | 0.135 | PRZYBLIZONE | +0.08 |
| Q-0042 | Runda rozmów USA–Iran do 07.10 | 0.483 | Polymarket (do 30.09, wysoki szczebel) | 0.435 | PRZYBLIZONE | −0.05 |
| Q-0054 | SR ≥ 5,00% | 0.940 | Polymarket | 0.99 | DOKLADNE | +0.05 |
| Q-0055 | AS wygrywa na Łotwie | 0.817 | Polymarket / Kalshi | 0.95 / 0.925 | DOKLADNE | +0.13 / +0.11 |
| Q-0056 | Lula > 50% w I turze | 0.063 | Manifold | 0.099 | DOKLADNE | +0.04 |
| Q-0058 | Przedłużenie rozejmu USA–ChRL do 07.10 | 0.450 | Kalshi / Polymarket (do 30.09–01.10) | 0.36 / 0.765 | PRZYBLIZONE | −0.09 / **+0.32** |
| Q-0065 | Uderzenie USA na Iran do 31.12 | 0.260 | Polymarket (zerwanie rozejmu) | 0.545 | PRZYBLIZONE | **+0.29** |
| Q-0066 | FOMC podnosi stopę 28.10 | 0.333 | Polymarket / Kalshi / Manifold | 0.65 / 0.67 / 0.618 | DOKLADNE | **+0.32 / +0.34 / +0.29** |
| Q-0073 | Pełna kontrola RU nad Kramatorskiem lub Słowiańskiem do 30.06.2027 | 0.117 | Polymarket (wejście, do 31.12) / Manifold | 0.19 / 0.147 | PRZYBLIZONE | +0.07 / +0.03 |

Nie znaleziono odpowiedników dla 47 pytań. Dotyczy to m.in. całego panelu ENE poza Brentem 06.10 (TTF, magazyny AGSI+, olej napędowy), CPI w PL, EUR/PLN, budżetu FR, ceł z H.R. 5334, magnesów, Blackwell, kabli bałtyckich, Kanału Panamskiego, KRLD w oknie 24.09–07.10, Tajwanu (nazwane ćwiczenia, MON ≥ 20 statków powietrznych, DSCA), 22. pakietu UE, aktywów Banku Rosji, Armenii i Azerbejdżanu.

## 3. Rozbieżności |AGR_RT − tłum| ≥ 0.20: hipotezy przyczyn

Hipotezy są robocze i przeznaczone do przeglądu. Nie rozstrzygają, kto ma rację.

**Dopasowania DOKLADNE**

1. **Q-0066 FOMC 28.10 (0.333 vs 0.62–0.67; trzy niezależne rynki zgodne).** Soczewki A i C założyły, że Fed odłoży podwyżkę na XII, bo posiedzenie wypada tydzień przed wyborami, a Biały Dom naciska. B przyjęła 50% szans na podwyżkę na kolejnym posiedzeniu cyklu. Rynki (Kalshi: wolumen ok. 770 tys. kontraktów) wyceniają ruch już w X. Hipoteza: soczewki nie miały wyceny kontraktów terminowych na stopę fed funds (np. FedWatch) i przeceniły argument wyborczy. To ten sam mechanizm Z1 („hamulec wyborczy”), który red team (05 §1 p. 1) wskazał jako ryzyko skorelowanego błędu.
2. **Q-0027 art. 4 NATO do 31.12 (0.113 vs 0.47; niska płynność, wolumen opcji ok. 7,5 tys. USD).** Soczewki oparły się na wysokim progu z 2026 r.: brak wniosku mimo drona nad Litwą. Rynek ekstrapoluje serię z IX 2025 (PL, EE) i widełki bid/ask są szerokie (0.41/0.53). Sama częstość bazowa nie tłumaczy wyceny: ok. 0,65/roku z lat 2022–2025 daje dla 3,3 mies. ok. 0,16, a nie 0,47. Hipoteza: różnica wynika z niskiej płynności albo z informacji o incydentach z ostatnich dni, której soczewki nie miały. Do sprawdzenia w etapie 01 wydania 02.
3. **Q-0001 mobilizacja RU (0.03 vs 0.26–0.27).** Manifold (17 graczy) i Polymarket (szersze kryterium) dają zbliżone wartości. Soczewki: koszt wewnętrzny, werbunek kontraktowy, częstość 1 dekret w 55 mies. Hipoteza: (a) na Polymarket liczy się też rozszerzenie kategorii w ramach dekretu z IX 2022, który formalnie nadal obowiązuje, a to zdarzenie znacznie tańsze dla Kremla niż nowy dekret; (b) na rynkach o wojnie widać premię za ogon (preferencję dla zakładów o mało prawdopodobne zdarzenia). Wiersz Manifold jest DOKLADNE, ale ma niską płynność.

**Dopasowania PRZYBLIZONE (poza wynikami; tylko do przeglądu)**

4. **Q-0030 Putin–Trump (0.267 vs 0.765 do 31.12).** Rynek lokalizacji daje Chinom 0.665. Rynek zakłada, że obaj będą na szczycie APEC w Shenzhen (18–19.11), a według kryterium rynku wystarczy uścisk dłoni. Soczewki traktowały spotkanie jako osobny szczyt wymagający postępu w rozmowach i nie rozważyły wspólnej obecności na APEC. Nasze kryterium („spotkają się osobiście, potwierdzą Kreml i Biały Dom”) prawdopodobnie obejmuje takie spotkanie. **To najpoważniejsza rozbieżność wydania: pominięty scenariusz, nie różnica w ocenie.** Do przeglądu: czy Q-0029 (Trump na APEC, 0.533) i Q-0030 są spójne. Jeśli Putin będzie w Shenzhen, P(Q-0030) ≈ P(Q-0029) × P(interakcja). Manifold (0.274) ma znikomą płynność i najpewniej nie uwzględnia tej informacji.
5. **Q-0026 spotkanie trójstronne (0.45 vs 0.035 Kalshi, szczebel przywódców; 0.645 Polymarket, RU–UA dowolny szczebel).** Rynki mierzą inne zdarzenia: przywódców albo kontakt dwustronny. Rozbieżność wynika z kryterium, nie z oceny. Nasze pytanie (delegacje, dowolny szczebel) leży między nimi.
6. **Q-0058 i Q-0011 rozejm USA–ChRL.** Polymarket (0.765 do 30.09) i Kalshi (0.36 do 01.10) różnią się między sobą o 0.40. Opcje Polymarket o krótkim terminie mają wolumen ok. 3–4 tys. USD, a kryteria obu rynków („nowe porozumienie celne”) mogą nie obejmować samego przedłużenia. Hipoteza: rynki są zbyt płytkie i zbyt odległe kryterialnie, żeby wskazać kierunek. Q-0011 na Kalshi (0.505 do 01.11) jest niżej niż nasze 0.75 prawdopodobnie dlatego, że przedłużenie może nastąpić 01–10.11 i może nie liczyć się jako „nowe porozumienie”.
7. **Q-0065 uderzenie USA na Iran (0.26 vs 0.545 zerwania rozejmu).** Wartość przeliczona z rynku „rozejm trwa do 31.12”. Zerwanie rozejmu może nastąpić przez działania Iranu albo bez uderzenia na ląd, więc rynek jest górną granicą dla naszego pytania. Mimo to rozbieżność jest duża. Hipoteza: rynek wycenia wyższe ryzyko zerwania po 03.11, zbieżnie z czerwoną flagą red teamu o Izraelu i założeniu Z1 (05 §1 p. 1–2).
8. **Q-0017 EBC (0.433 vs ≥ 0.64).** Rynek XII ma płynność ok. 4 tys. USD i szerokie widełki. Rynek X (0.48, płynność ok. 41 tys. USD) jest bliżej nas. Soczewka B wspomniała, że kontrakty wyceniają ok. 3 podwyżki do połowy 2027, ale uśredniła to z konsensusem ekonomistów. Hipoteza: soczewki przeważyły opinię ekonomistów względem wyceny rynkowej.
9. **Q-0018 bank z ChRL na SDN (0.087 vs 0.315).** Rynek Kalshi ma 145 kontraktów wolumenu, a jego kryterium jest szersze: dowolne sankcje Skarbu, w tym FinCEN, bez wymogu powodu Iran/Rosja. Rozbieżność nieinformatywna.

**Rozbieżności poniżej progu, warte odnotowania.** Q-0033 Lula: trzy rynki dają 0.37–0.44 wobec naszych 0.557, a GJO 0.50. Przy wysokiej płynności (Polymarket: ok. 20 mln USD) różnica 0.12–0.18 jest spójna między rynkami. Hipoteza: soczewki oparły się na sondażach II tury „w granicach błędu” (Quaest), a rynki ważą trend spadkowy Luli. Q-0055 Łotwa: rynki 0.93–0.95 wobec 0.817.

## 4. Kontrola spójności benchmarków

- Niespójność międzyrynkowa dla Ormuzu: Polymarket P(średnia ≥ 60) = 0.205 jest wyższe niż Kalshi P(> 40) = 0.18, choć zdarzenie Polymarket jest węższe. Do wyników wchodzi tylko Kalshi (DOKLADNE).
- Q-0036 i Q-0037 (Ormuz) oraz Q-0031 (Izba) mają AGR_RT w przedziale wyznaczonym przez rynki albo blisko niego. Q-0006 (Brent) różni się o 0.02.
- Do wyników (BSS vs tłum) wejdzie 12 pytań z dopasowaniem DOKLADNE: Q-0001, Q-0006, Q-0020, Q-0027, Q-0031, Q-0033, Q-0036, Q-0037, Q-0054, Q-0055, Q-0056, Q-0066. Gdy jedno pytanie ma kilka źródeł, `wyniki.py` uśrednia je.

## 5. Zgłoszenia

- Nie zmieniono żadnej prognozy. Nie logowano się do żadnego serwisu.
- W treściach stron i odpowiedziach API nie znaleziono instrukcji wstrzykniętych.
- Uwaga procesowa do przeglądu kwartalnego: Metaculus nie jest dostępny bez konta, a RAND Forecasting Initiative jest zamknięta. Z sześciu źródeł z metodologii §6 realnie działają cztery.
