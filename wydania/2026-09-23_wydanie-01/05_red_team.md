# Etap 05 — Red team (wydanie 01, stan 23.09.2026)

Wejście: `03_analiza.md`, `04_prognozy_A.md`, `04_prognozy_B.md`, `04_prognozy_C.md`, `02_fakty/G1–G4.md`, `rejestr/pytania.csv`, `rejestr/prognozy.csv` (przebiegi A, B, C). Nie otwierano plików `06_*`, `07_zalacznik_benchmarki.md`, `rejestr/benchmarki.csv` ani serwisów prognostycznych. Wyszukiwania: 4 + 1 pobranie (weryfikacja faktów, z blokadą domen z CLAUDE.md p. 9; UKMTO — HTTP 403).
Rola: obalić, nie potwierdzić. Korekty tylko z konkretnym dowodem albo błędem logicznym, limit ±0.15 na pytanie (metodologia §5).
Konwencja: AGR = średnia A, B, C (3 miejsca po przecinku); AGR_RT = AGR + korekta, zaokrąglone do 0.01. Bez korekty AGR_RT = AGR (etap 06).

---

## 1. Dziesięć najsłabszych punktów analizy

| # | Słaby punkt | Typ | Dowód lub argument | Pytania, na które wpływa |
|---|---|---|---|---|
| 1 | **Jeden mechanizm tłumaczy za dużo: „hamulec wyborczy 03.11”.** Założenie Z1 i soczewki A i C wyjaśniają nim ok. 10 pytań naraz (C sama wymienia 7). Test lustra w 03 (§1.6 p. 6) wskazał logikę przeciwną (szybka operacja mobilizuje wyborców), ale żadna soczewka jej nie rozważyła. Oparcie: seria 15 okresów bez uderzeń (G1-005, źródło C/3) i doniesienie Interii o porozumieniu „po wyborach” (G4-055, relacja z drugiej ręki). | założenie bez dowodu; lustro | Błąd tego założenia przesunie wszystkie pytania naraz — ryzyko skorelowanego błędu w klastrach IRAN_WOJNA, ORMUZ, ROPA_CENA, BAB_EL_MANDAB. Nie koryguję (brak dowodu przeciwnego), ale wynik tych pytań trzeba czytać jako jeden zakład. | Q-0007, Q-0012, Q-0028, Q-0038, Q-0041, Q-0065, Q-0068 |
| 2 | **Pominięty aktor: Izrael.** Analiza wojny z Iranem (A, B, ACH-1, W1–W5) nie wymienia Izraela jako strony zdolnej do samodzielnego uderzenia albo do zerwania toru USA–Iran; w 02 występuje tylko w kontekście Libanu i Gazy (G1-063, G4-014). Pezeszkian w ONZ 23.09 mówi wprost o Izraelu (fakty dodatkowe A). | pominięty aktor | Uderzenie Izraela nie rozstrzyga Q-0041/Q-0065 (tylko USA), ale może zerwać rozmowy i podbić ropę — ACH-1 ma lukę po stronie H3. | Q-0007, Q-0028, Q-0038, Q-0042, Q-0063 |
| 3 | **Ormuz: obie serie pomiarowe pochodzą od stron sporu albo z agregatów.** CENTCOM/UKMTO (G2-006) to strona konfliktu oznaczona jako perspektywa Z; PortWatch przychodzi przez agregat Straits Daily Brief (G1-001, C/2), nie z IMF bezpośrednio. Brak niezależnej perspektywy T. Pytania Q-0036 i Q-0037 są rozstrzygane PortWatch (AIS), a więc mierzą ruch „jawny”, nie scenariusz H4. | źródła jednej strony | Soczewki prawidłowo trzymają Q-0036/Q-0037 nisko; nie koryguję. Ryzyko: Q-0037 = NIE nawet przy H4. | Q-0036, Q-0037 |
| 4 | **Brak danych potraktowany jak brak zdarzeń.** 03 §1.7 p. 10 zapisuje lukę: „brak danych o atakach Huti na statki handlowe w IX”. Wszystkie trzy soczewki obniżają Q-0062 właśnie z tego powodu (A: „brak danych… sugeruje”; B: „kor. w dół — brak znalezionych incydentów”; C: „brak danych”). Luka w zbieraniu to nie dowód spokoju. Podobnie Q-0047 (brak raportów MON Tajwanu 15–23.09). | przereagowanie na brak nagłówków | Korekta Q-0062 (tabela §3). Q-0047 — bez korekty (p_status_quo 0.50 już to odzwierciedla). | Q-0062, Q-0047 |
| 5 | **Przegląd postawy USA: kongresowy „hamulec” przeceniony.** Soczewki A i C traktują §1249 NDAA jako blokadę. G1-031 mówi co innego: §1249 zakazuje redukcji poniżej 76 tys. na ponad 45 dni *bez certyfikacji* sekretarza obrony i dowódcy EUCOM, a wg analizy (grosswald.org) próg może nie obowiązywać od 01.10 do uchwalenia NDAA FY2027 (C-10: projekt §1232 — też próg z certyfikacją). To procedura, nie zakaz. Ponadto ACH-3 w 03 wskazuje jako najmniej obalone H1 i H2 — obie hipotezy zakładają redukcję; H3 (status quo) osłabiają opcje liczbowe i precedens z V 2026. | założenie bez dowodu; spójność ze scenariuszem | Korekta Q-0003 (§3). | Q-0003, Q-0044 |
| 6 | **Baza USA w Polsce: źródła wyłącznie polskie i prezydenckie.** Trump, Nawrocki i MON (G1-025…027); brak szczegółów Pentagonu i liczby stanu osobowego (03 §1.7 p. 4). Z tego wynika sygnał „przeciwny” w W13 — nie jest potwierdzony. | źródła jednej strony | Q-0044 (0.20) nie wymaga korekty; W13 nie powinno równoważyć redukcji w Europie bez liczby żołnierzy. | Q-0044, Q-0003 |
| 7 | **Front UA: rozbieżne serie tempa, a soczewki wybrały jedną.** G1-044 podaje trzy wartości: DeepState ok. 150 km²/4 tyg., The Economist ok. 78 km²/30 dni (15.09) i ok. 200 km² (08.09). A i B liczą tempo „36–150 km²/mies.”, pomijając odczyt ok. 200 km². Uzasadnienie C („rasputica… wymaga przyspieszenia”) wskazuje na NIE, a C daje najwyższe p (0.35) — niespójność wewnętrzna soczewki. Dwa błędy działają w przeciwne strony. | źródło jednej serii; niespójność | Bez korekty Q-0004 (błędy się znoszą, AGR 0.227 mieści się między CB B a odczytem 200 km²). | Q-0004, Q-0073 |
| 8 | **Nieaktualny fakt w soczewce A: Węgry jako blokujący sankcje.** A (Q-0019): „Francja, Słowacja i Węgry wymuszają ustępstwa”. C-13 (RFE/RL 08.09): po zmianie rządu na Węgrzech (V 2026) rolę blokującego przejęła Słowacja. 03 tej zmiany nie odnotowuje. | przestarzałe założenie | Kierunek wpływu niejednoznaczny (mniej blokujących, ale Słowacja potrafiła opóźnić 18. pakiet o ok. 5 tyg.). Bez korekty. | Q-0019, Q-0071 |
| 9 | **Magazyny gazu: błąd rachunkowy w C-12 (soczewka C).** C: „do 80% na 01.11 potrzeba ok. 5,5 TWh/d wobec ok. 2,8 TWh/d”. Z G2-017: brakuje 9,7 pp × ok. 1130 TWh ≈ 110 TWh w 40 dni ≈ 2,7 TWh/d — czyli tyle, ile wynosi obecne tłoczenie (2790 GWh/d). 5,4 TWh/d to wg G2-017 wymóg dla celu **90%**. Próg 80% jest osiągalny, jeśli tempo nie spadnie; projekcja 78,2% (G2-018) zakłada spadek. | błąd w danych | C = 0.30 oparła się częściowo na błędzie, ale A (0.30) doszła do tej samej wartości innym tokiem, a B (0.45) ma poprawną ekstrapolację. AGR 0.35 pozostaje w rozsądnym przedziale 0.30–0.45 — bez korekty. | Q-0067, Q-0049, Q-0010 |
| 10 | **Nadinterpretacja pojedynczych obserwacji jako sygnałów intencji.** (a) Eksport magnesów −21% m/m w VIII jako „sygnał przed szczytem” (03 §A, pewność niska co do intencji) — soczewki A i C budują na tym Q-0025; B słusznie wskazuje powrót do średniej (I–VIII +23% r/r). (b) „Druga runda 23.09” — w The National tylko „prawdopodobnie”, A używa tego w Q-0006 jak faktu. (c) Oferta otwarcia Ormuzu „w 7 dni” (G1-007) — sporna, dementowana przez IRGC. | przereagowanie na nagłówki | Bez korekt: wpływ na AGR mały, a B równoważy A i C w Q-0025. | Q-0025, Q-0006, Q-0037 |

Uwagi dodatkowe (poniżej progu dziesięciu):
- **Ekspozycja ślepoty soczewki B** (dziennik 04-B): B widziała wiersze A dla Q-0001 i Q-0002 i dała dokładnie te same wartości (0.03, 0.05). Dla Q-0001 korekta B w dół (0.06 → 0.03) ma własne uzasadnienie (werbunek kontraktowy). Dla Q-0002 korekta B (0.07 → 0.05) z powodu „braku zdarzenia mimo wielu incydentów” liczy ten sam dowód drugi raz — reguła Laplace’a (0 zdarzeń w 43 mies.) już go zawiera. Korekta +0.01 w §3.
- **Soczewka C, Q-0031:** uzasadnienie („Demokratom brakuje ok. 3–5 mandatów”, poparcie Trumpa 39%) wskazuje na p niższe niż 0.20. Korekta w §3.
- **Soczewka A, Q-0039:** „soczewka nic tu nie mówi”, a mimo to p = 0.35, najwyżej ze wszystkich trzech — bez oparcia w danych hydrologicznych.
- 03 §1.6 B słusznie wymienia liczby wojenne stron (MO FR, SG ZSU, Huti) jako niepewne. Soczewki się do tego stosują (np. > 45% mocy rafinerii tylko jako „wg SG ZSU”).

---

## 2. Przegląd prognoz

### 2.1 AGR dla wszystkich pytań

| ID | A | B | C | AGR | rozrzut | ID | A | B | C | AGR | rozrzut |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q-0001 | 0.03 | 0.03 | 0.03 | 0.030 | 0.00 | Q-0038 | 0.32 | 0.22 | 0.30 | 0.280 | 0.10 |
| Q-0002 | 0.05 | 0.05 | 0.05 | 0.050 | 0.00 | Q-0039 | 0.35 | 0.10 | 0.20 | 0.217 | 0.25 |
| Q-0003 | 0.35 | 0.35 | 0.30 | 0.333 | 0.05 | Q-0040 | 0.40 | 0.75 | 0.55 | 0.567 | **0.35** |
| Q-0004 | 0.18 | 0.15 | 0.35 | 0.227 | 0.20 | Q-0041 | 0.05 | 0.08 | 0.05 | 0.060 | 0.03 |
| Q-0005 | 0.25 | 0.35 | 0.40 | 0.333 | 0.15 | Q-0042 | 0.55 | 0.45 | 0.45 | 0.483 | 0.10 |
| Q-0006 | 0.35 | 0.45 | 0.40 | 0.400 | 0.10 | Q-0043 | 0.40 | 0.35 | 0.35 | 0.367 | 0.05 |
| Q-0007 | 0.12 | 0.25 | 0.20 | 0.190 | 0.13 | Q-0044 | 0.20 | 0.20 | 0.20 | 0.200 | 0.00 |
| Q-0008 | 0.15 | 0.30 | 0.15 | 0.200 | 0.15 | Q-0045 | 0.25 | 0.15 | 0.15 | 0.183 | 0.10 |
| Q-0009 | 0.25 | 0.35 | 0.30 | 0.300 | 0.10 | Q-0046 | 0.50 | 0.45 | 0.40 | 0.450 | 0.10 |
| Q-0010 | 0.40 | 0.25 | 0.40 | 0.350 | 0.15 | Q-0047 | 0.40 | 0.40 | 0.55 | 0.450 | 0.15 |
| Q-0011 | 0.72 | 0.75 | 0.78 | 0.750 | 0.06 | Q-0048 | 0.35 | 0.37 | 0.40 | 0.373 | 0.05 |
| Q-0012 | 0.20 | 0.15 | 0.22 | 0.190 | 0.07 | Q-0049 | 0.70 | 0.60 | 0.55 | 0.617 | 0.15 |
| Q-0013 | 0.80 | 0.85 | 0.88 | 0.843 | 0.08 | Q-0050 | 0.30 | 0.35 | 0.35 | 0.333 | 0.05 |
| Q-0014 | 0.55 | 0.55 | 0.58 | 0.560 | 0.03 | Q-0051 | 0.30 | 0.30 | 0.25 | 0.283 | 0.05 |
| Q-0015 | 0.12 | 0.12 | 0.08 | 0.107 | 0.04 | Q-0052 | 0.45 | 0.47 | 0.45 | 0.457 | 0.02 |
| Q-0016 | 0.15 | 0.10 | 0.30 | 0.183 | 0.20 | Q-0053 | 0.50 | 0.45 | 0.52 | 0.490 | 0.07 |
| Q-0017 | 0.45 | 0.45 | 0.40 | 0.433 | 0.05 | Q-0054 | 0.85 | 0.68 | 0.93 | 0.820 | 0.25 |
| Q-0018 | 0.10 | 0.08 | 0.08 | 0.087 | 0.02 | Q-0055 | 0.75 | 0.88 | 0.82 | 0.817 | 0.13 |
| Q-0019 | 0.55 | 0.50 | 0.40 | 0.483 | 0.15 | Q-0056 | 0.08 | 0.04 | 0.07 | 0.063 | 0.04 |
| Q-0020 | 0.30 | 0.25 | 0.20 | 0.250 | 0.10 | Q-0057 | 0.12 | 0.12 | 0.15 | 0.130 | 0.03 |
| Q-0021 | 0.63 | 0.70 | 0.72 | 0.683 | 0.09 | Q-0058 | 0.45 | 0.45 | 0.45 | 0.450 | 0.00 |
| Q-0022 | 0.60 | 0.72 | 0.72 | 0.680 | 0.12 | Q-0059 | 0.15 | 0.10 | 0.10 | 0.117 | 0.05 |
| Q-0023 | 0.35 | 0.50 | 0.45 | 0.433 | 0.15 | Q-0060 | 0.55 | 0.68 | 0.45 | 0.560 | 0.23 |
| Q-0024 | 0.15 | 0.15 | 0.20 | 0.167 | 0.05 | Q-0061 | 0.25 | 0.15 | 0.25 | 0.217 | 0.10 |
| Q-0025 | 0.45 | 0.60 | 0.45 | 0.500 | 0.15 | Q-0062 | 0.45 | 0.45 | 0.40 | 0.433 | 0.05 |
| Q-0026 | 0.45 | 0.45 | 0.45 | 0.450 | 0.00 | Q-0063 | 0.45 | 0.40 | 0.40 | 0.417 | 0.05 |
| Q-0027 | 0.10 | 0.12 | 0.12 | 0.113 | 0.02 | Q-0064 | 0.25 | 0.25 | 0.30 | 0.267 | 0.05 |
| Q-0028 | 0.35 | 0.25 | 0.30 | 0.300 | 0.10 | Q-0065 | 0.25 | 0.28 | 0.25 | 0.260 | 0.03 |
| Q-0029 | 0.50 | 0.60 | 0.50 | 0.533 | 0.10 | Q-0066 | 0.30 | 0.40 | 0.30 | 0.333 | 0.10 |
| Q-0030 | 0.30 | 0.25 | 0.25 | 0.267 | 0.05 | Q-0067 | 0.30 | 0.45 | 0.30 | 0.350 | 0.15 |
| Q-0031 | 0.15 | 0.12 | 0.20 | 0.157 | 0.08 | Q-0068 | 0.25 | 0.25 | 0.20 | 0.233 | 0.05 |
| Q-0032 | 0.15 | 0.12 | 0.15 | 0.140 | 0.03 | Q-0069 | 0.15 | 0.15 | 0.20 | 0.167 | 0.05 |
| Q-0033 | 0.55 | 0.57 | 0.55 | 0.557 | 0.02 | Q-0070 | 0.30 | 0.33 | 0.30 | 0.310 | 0.03 |
| Q-0034 | 0.30 | 0.35 | 0.35 | 0.333 | 0.05 | Q-0071 | 0.20 | 0.12 | 0.20 | 0.173 | 0.08 |
| Q-0035 | 0.08 | 0.10 | 0.10 | 0.093 | 0.02 | Q-0072 | 0.12 | 0.15 | 0.12 | 0.130 | 0.03 |
| Q-0036 | 0.30 | 0.20 | 0.22 | 0.240 | 0.10 | Q-0073 | 0.10 | 0.10 | 0.15 | 0.117 | 0.05 |
| Q-0037 | 0.10 | 0.12 | 0.12 | 0.113 | 0.02 | | | | | | |

Pięć pytań z identycznymi p we wszystkich soczewkach (Q-0001, Q-0002, Q-0026, Q-0044, Q-0058) — możliwe zakotwiczenie na wspólnym wejściu (03); dla Q-0001 i Q-0002 dodatkowo zgłoszona ekspozycja B na wiersze A.

### 2.2 AGR niespójny z faktami z `02_fakty` (i faktami dociągniętymi w etapie 04)

| ID | AGR | Niespójność | Źródło |
|---|---|---|---|
| Q-0054 | 0.820 | Soczewki A i B nie znały odczytu po 97,64% protokołów (5,13%, C-01; w mojej weryfikacji 23.09 nie znalazłem tej liczby — potwierdzone jest 5,00% przy 96,95%, RIA/Meduza). Meduza 22.09: analityk wyborczy wskazuje, że SR „dopisano ok. 60 tys. głosów” na ostatnim etapie — sygnał decyzji administracyjnej o wejściu SR do Dumy (fakt o wypowiedzi, interpretacja sporna). Trend doliczania + decyzja polityczna → B (0.68, czysta ekstrapolacja) jest zaniżona. | G4-028; C-01; Meduza 22.09 |
| Q-0013 | 0.843 | Rachunek wszystkich trzech soczewek daje +0,8–1,0 pp do wskaźnika m/m z samych paliw. Efekt bazy: w IX 2025 CPI m/m wyniósł 0,0% (GUS, szybki szacunek i dane ostateczne), więc zmiana r/r ≈ zmiana m/m w IX 2026. Z 3,4% daje to ok. 4,2–4,4% r/r. Aby wynik spadł poniżej 3,5%, reszta koszyka musiałaby dać ok. −0,7 do −0,9 pp m/m (w IX 2025 żywność: −0,5% m/m, tj. ok. −0,13 pp wkładu). Soczewki nie uzasadniają ok. 16% szans na NIE. | G2-022, G3-027, C-06; GUS IX 2025 |
| Q-0050 | 0.333 | A i B oparły się na 8,89 zł/l (16.09); notowanie e-petrol z 23.09 to 8,99 zł/l (C-04), 1 gr poniżej progu. Kierunek na 2 tygodnie: obniżka hurtu Orlenu 23.09 i sześć sesji spadku Brent działają w dół. | G2-024; C-04 |
| Q-0039 | 0.217 | A (0.35) nie podaje żadnych danych. B zna je: ACP obniża zanurzenie od 01.10 (zaostrzenie, nie luzowanie), opady V–VIII −34%, El Niño do 2027; w suszy 2023–24 limit zaostrzano do XI i luzowano dopiero w 2024. | G1-058; fakty B (DTN, Maritime Executive) |
| Q-0062 | 0.433 | Brak danych za IX (luka) soczewki potraktowały jak brak zdarzeń. Kryterium obejmuje abordaż w Zatoce Adeńskiej, a wg B (VII–VIII: 05.07 Hodejda, VIII „Amzan”, 20.08 abordaż Seamull 136 Mm od Al-Mukalli) tempo to 2–3 zdarzenia/mies. → 14 dni ≈ 0,6–0,7 przy stałym tempie. Po zakończeniu monsunu południowo-zachodniego (IX) piractwo somalijskie sezonowo rośnie (OCENA, pewność: średnia). Weryfikacja 23.09: brak znalezionych komunikatów UKMTO z IX (strona UKMTO — HTTP 403), więc luka nadal otwarta. | G1-023, §1.7 p. 10 w 03; fakty B |

### 2.3 Niespójności logiczne między pytaniami

Sprawdzone relacje:

| Relacja | Wartości AGR | Wynik |
|---|---|---|
| Q-0058 (do 07.10) ≤ Q-0011 (do 10.11) — to samo zdarzenie, krótszy termin | 0.450 ≤ 0.750 | spójne |
| Q-0041 (2 tyg.) ≤ Q-0065 (do 31.12) | 0.060 ≤ 0.260 | spójne |
| Q-0021 ≤ Q-0011 (przedłużenie zawieszenia kontroli zwykle w pakiecie z rozejmem) | 0.683 ≤ 0.750 → P(Q-0021 \| Q-0011) ≈ 0,9 | spójne; zob. §5 (ACH-2) |
| Q-0022 ≈ Q-0021 (ten sam pakiet, dłuższy termin) | 0.680 vs 0.683 | spójne |
| Q-0038 (zniesienie blokady) ≤ Q-0028 (porozumienie) + premia za zawieszenie bez porozumienia | 0.280 vs 0.300 | spójne |
| Q-0036 (PortWatch > 40) ≤ P(porozumienie) × P(odbudowa ruchu AIS) + otwarcie de facto | 0.240 vs 0.30 × ok. 0,6 + ok. 0,05 ≈ 0,23 | spójne |
| Q-0008 (Brent < 80) vs Q-0028: spadek < 80 bez porozumienia mało prawdopodobny | 0.200 vs 0.300 | na granicy (implikuje P(< 80 \| porozumienie) ≈ 0,5–0,6); bez korekty — model zmienności B jest uzasadniony |
| Q-0007 + Q-0008 (dwa przeciwne ogony, oba możliwe w 3 mies.) | 0.19 + 0.20 = 0.39 | spójne |
| Q-0026 (spotkanie trójstronne) ≥ Q-0059 (rozejm energetyczny, 2 tyg.) | 0.450 ≥ 0.117 | spójne |
| Q-0033 (Lula wygrywa) ≥ Q-0056 (Lula > 50% w I turze) | 0.557 ≥ 0.063 | spójne |
| Ścieżka magazynów: Q-0049 (> 73% 06.10) → Q-0067 (≥ 80% 01.11) → Q-0010 (< 55% 01.01) | 0.617 / 0.350 / 0.350 | spójne (ścieżka ok. 73,5% → ok. 78–79% → ok. 55–58%) |
| Q-0023 (wpis MOFCOM) vs wyzwalacze Q-0069 (DSCA ≥ 1 mld) i Q-0012 (cła H.R. 5334) | 0.433 vs 0.167, 0.190 | spójne (wpisy mogą mieć też inne powody) |
| Q-0013 (CPI ≥ 3,5%) vs Q-0016 (zmiana stóp RPP) | 0.843 (po korekcie 0.94) vs 0.183 | napięcie, nie sprzeczność: CPI ok. 4,3% jest powyżej pasma celu (2,5 ± 1), ale prezes RPP zapowiada stabilizację (G3-027). Bez korekty Q-0016 — C (0.30) ma dowód (C-07), A i B mają dowód przeciwny (G3-027). |

Nie znaleziono pary pytań wykluczających się z sumą > 1 ani przypadku P(A i B) > P(A).

### 2.4 Rozrzut soczewek > 0.30

Tylko **Q-0040** (Bałtyk — kabel lub rurociąg ze śledztwem do 31.03.2027): A 0.40, B 0.75, C 0.55.
- **B ma lepsze podstawy.** Jawna klasa odniesienia: w każdej z trzech ostatnich zim co najmniej jeden taki incydent ze śledztwem lub zatrzymaniem statku (Balticconnector X 2023; Eagle S XII 2024; Fitburg 31.12.2025 — fakt B: Euronews, The Moscow Times; od X 2023 co najmniej 11 uszkodzonych kabli). Okno pytania obejmuje cały sezon X–III.
- **A** podaje mechanizm („flota cieni zimą”, „szybkie postępowania”), który wspiera TAK, a mimo to p = 0.40 — uzasadnienie nie zawiera argumentu za NIE poza „niska pewność”. **C** sama oznacza soczewkę jako słabą.
- Kontrargument dla B: wzmocnione patrole NATO od 2025 (Baltic Sentry) i duńskie inspekcje (G1-062) mogą obniżać częstość — B już to uwzględnia (0.80 → 0.75).
- Wniosek: korekta w górę (§3), ale nie do poziomu B — trzy obserwacje to mała próba.

Rozrzuty 0.20–0.25 (poniżej progu, dla porządku): Q-0039 (A bez danych — korekta), Q-0054 (B bez faktu C-01 — korekta), Q-0060 (A/C vs B — różnica w ocenie długości pauzy OFAC po wizycie Xi; obie strony mają argument, bez korekty), Q-0004 i Q-0016 (§1 p. 7, §2.3).

---

## 3. Propozycje korekt AGR

| ID | AGR | proponowana korekta | AGR_RT | uzasadnienie | typ |
|---|---|---|---|---|---|
| Q-0054 | 0.820 | +0.12 | 0.94 | Wynik SR rósł z liczeniem (4,96% → 5,00%; wg C-01 5,13% przy 97,64%). Meduza 22.09: dopisanie ok. 60 tys. głosów na ostatnim etapie (interpretacja sporna, ale wskazuje decyzję o wejściu SR). Soczewka B (0.68) nie miała C-01; A i C (0.85, 0.93) mają lepsze podstawy. Zostawiam ok. 6% na nieprzewidywalność ostatecznego protokołu CKW. | dowód |
| Q-0013 | 0.843 | +0.10 | 0.94 | Rachunek soczewek: paliwa +0,8–1,0 pp m/m; baza IX 2025 = 0,0% m/m (GUS) → r/r ok. 4,2–4,4%. NIE wymaga ok. −0,8 pp m/m z pozostałej części koszyka — w IX 2025 sama żywność dała tylko ok. −0,13 pp. Soczewki nie podały argumentu za NIE, który odpowiadałby 16%. | logika (niespójność rachunku z p) + dowód (baza GUS) |
| Q-0040 | 0.567 | +0.10 | 0.67 | Jedyny rozrzut > 0.30. Klasa odniesienia B (3 z 3 zim z incydentem i śledztwem) jest udokumentowana. A nie podaje argumentu za NIE. Korekta tylko do ok. połowy odległości do B — mała próba i wzmocnione patrole. | dowód |
| Q-0003 | 0.333 | +0.07 | 0.40 | (1) Soczewki A i C traktują §1249 jako hamulec, a G1-031 opisuje procedurę certyfikacji (nie zakaz), i to z możliwą luką po 30.09. (2) ACH-3 w 03: najmniej obalone H1 i H2 — obie zakładają redukcję w Europie; opcje 25–40 tys. (G1-030) przekraczają próg 10 tys. z zapasem; precedens z V 2026 (5 tys. z Niemiec). AGR 0.333 zakłada, że status quo lub odroczenie poza 31.03.2027 jest dwa razy bardziej prawdopodobne niż decyzja — sprzeczne z ACH-3. Korekta umiarkowana, bo rekomendacja dopiero 06.11, a H1 może oznaczać redukcję netto < 10 tys. | dowód + spójność |
| Q-0062 | 0.433 | +0.08 | 0.51 | Wszystkie soczewki obniżyły p z powodu braku danych za IX — to luka w zbieraniu (03 §1.7 p. 10), nie obserwacja. Tempo z VII–VIII 2–3 zdarzenia/mies. (w tym abordaże, które kryterium liczy) → ok. 0,6–0,7 dla 14 dni. Korekta mniejsza od pełnej, bo blokada Huti mogła faktycznie działać przez odstraszanie (A). | logika |
| Q-0039 | 0.217 | −0.07 | 0.15 | A (0.35) bez danych („soczewka nic tu nie mówi”). Dane B: ACP zaostrza (zanurzenie od 01.10), opady −34%, El Niño do 2027, analogia 2023–24: zaostrzenia trwały przez porę deszczową. Nic w 02 nie wskazuje na poprawę stanu jeziora Gatún do 31.10. | dowód |
| Q-0031 | 0.157 | −0.05 | 0.11 | Uzasadnienie C (0.20): Demokratom brakuje 3–5 mandatów (G4-035), poparcie Trumpa 39%, generic ballot D +7–8 — wszystko to przemawia za niższym p, a C nie podaje argumentu za wyższym. Klasa odniesienia B (partia prezydenta z poparciem < 45% traci co najmniej kilka mandatów niemal w każdych wyborach połówkowych) daje ok. 0.10–0.12. Zmiany map okręgów (Missouri) już ujęte w B. | logika (niespójność uzasadnienia C) |
| Q-0050 | 0.333 | +0.05 | 0.38 | A i B wyszły od 8,89 zł/l (16.09); stan 23.09: 8,99 zł/l (C-04), próg 9,00. Korekta tylko częściowa: hurt Orlen obniżony 23.09, a Brent spada — detal zwykle idzie za hurtem z opóźnieniem ok. tygodnia. | dowód |
| Q-0002 | 0.050 | +0.01 | 0.06 | B: reguła Laplace’a (0 zdarzeń w 43 mies.) → 0,07, potem korekta w dół „brak zdarzenia mimo wielu incydentów” — ten sam dowód policzony drugi raz. Po usunięciu podwójnego liczenia B = 0.07, AGR ≈ 0.057. Ponadto B widziała wartość A przed prognozą (dziennik 04-B). | logika |

Pozostałe 64 pytania: **bez korekty** (AGR_RT = AGR). Brak korekt „dla bezpieczeństwa” i w stronę 0.5 bez powodu: 5 z 9 korekt oddala p od 0.5 (Q-0054, Q-0013, Q-0040, Q-0039, Q-0031); 4 zbliżają (Q-0003, Q-0062, Q-0050, Q-0002) — każda z konkretnym dowodem albo wskazanym błędem.

Rozważone i odrzucone (brak dowodu wystarczającego do korekty): Q-0004 (§1 p. 7), Q-0016 (§2.3), Q-0067 (§1 p. 9), Q-0070 (kalendarz Fitch 2027 nieznany — zwykle luty, w oknie; A, B, C zbieżne), Q-0055 (B 0.88 na średniej sondaży PolitPro; A 0.75 bez nowego dowodu; rozrzut 0.13), Q-0060 (§2.4), Q-0008 (§2.3).

Kontrola trywialności (§3.8) po korektach: AGR_RT < 0.05 lub > 0.95 — 1 pytanie (Q-0001, 0.03) = 1,4% aktywnych (limit 20%). Q-0013 i Q-0054 (0.94) poniżej progu 0.95.

---

## 4. Test skrzywienia kierunkowego

Wszystkie pytania z czyj_sukces ≠ BRAK mają p_status_quo = 0.10 (TAK wymaga zmiany).

| czyj_sukces | n | śr. p_status_quo | śr. AGR | śr. AGR_RT | AGR − SQ | Pytania |
|---|---|---|---|---|---|---|
| USA_ZACHOD | 1 | 0.10 | 0.167 | 0.17 | +0.07 | Q-0069 |
| UE | 1 | 0.10 | 0.483 | 0.48 | +0.38 | Q-0019 |
| UKRAINA | 2 | 0.10 | 0.220 | 0.22 | +0.12 | Q-0064 (0.267), Q-0071 (0.173) |
| ROSJA | 3 | 0.10 | 0.226 | 0.25 | +0.13 (RT: +0.15) | Q-0003 (0.333), Q-0004 (0.227), Q-0073 (0.117) |
| CHINY | 1 | 0.10 | 0.167 | 0.17 | +0.07 | Q-0024 |
| KOMPROMIS | 7 | 0.10 | 0.444 | 0.44 | +0.34 | Q-0011 (0.75), Q-0021 (0.683), Q-0022 (0.68), Q-0058 (0.45), Q-0028 (0.30), Q-0072 (0.13), Q-0059 (0.117) |
| BRAK | 58 | 0.169 | 0.331 | 0.34 | — | — |

Bloki: strona zachodnia (USA_ZACHOD + UE + UKRAINA, n = 4): śr. AGR 0.273; strona rosyjsko-chińska (ROSJA + CHINY, n = 4): śr. AGR 0.211 (po korekcie Q-0003: 0.228). Grupa IRAN — 0 pytań.

**Wniosek (pewność: niska — n = 4 na blok).** Brak systematycznego faworyzowania którejś strony. Różnica bloków (ok. 0.05–0.06) wynika w całości z jednego pytania: Q-0019 (22. pakiet UE, 0.483). To pytanie ma realne oparcie proceduralne: rytm pakietów co ok. 2,6 mies. i 4–6 tyg. od propozycji do przyjęcia. Bez Q-0019 blok zachodni ma 0.202 — mniej niż rosyjsko-chiński. Wszystkie grupy leżą powyżej p_status_quo, bo SQ = 0.10 jest mechaniczne i nie uwzględnia zapowiedzianych decyzji.
**KOMPROMIS** odbiega najmocniej od SQ (+0.34). Przyczyna: Q-0011, Q-0021, Q-0022 pytają o przedłużenie istniejącego rozejmu. Formalnie TAK wymaga nowej decyzji (SQ 0.10), ale w praktyce przedłużenie jest kontynuacją stanu. To cecha konstrukcji p_status_quo (§3.5), nie skrzywienie prognoz. Uwaga do przeglądu kwartalnego: BSS względem SQ na tych pytaniach będzie bardzo wrażliwy na jedno rozstrzygnięcie.
Kontrola odwrotna: pytania, w których AGR mógłby odzwierciedlać zachodnie „myślenie życzeniowe”, to Q-0071 (aktywa Banku Rosji) i Q-0064 (umowa dronowa). Oba mają niskie AGR z uzasadnieniem przeciwnym życzeniu — skrzywienia nie widać.

---

## 5. Spójność ze scenariuszami analizy

Etap 03 nie podaje liczbowych prawdopodobieństw scenariuszy (reguła etapu). Porównuję więc prognozy z jakościowymi wnioskami ACH i oceną scenariuszy z §1.2.

| Wniosek analizy | Implikacja w prognozach | Ocena |
|---|---|---|
| Scenariusz bazowy (BAZ „przewlekły kryzys bez rozstrzygnięć”) pozostaje trafny (§1.2) | Porozumienie USA–Iran do 31.12: 0.30; uderzenie USA: 0.26; Brent > 120: 0.19; Brent < 80: 0.20; TTF > 90: 0.30; rozejm USA–ChRL przedłużony: 0.75; spotkanie Putin–Trump: 0.27 | **spójne** — każdy wyznacznik KOR i KRY ma p < 0.35, BAZ dominuje |
| ACH-1 (Iran): najmniej obalona H2 (zamrożenie), potem H4; H1 osłabiona, H3 osłabiona | H1 ≈ Q-0028 = 0.30; H3 ≈ Q-0065 = 0.26; H2+H4 ≈ 0.44 | **spójne co do kolejności**; zastrzeżenie §1 p. 2 (Izrael) — H3 może być niedoszacowana, ale bez dowodu nie koryguję |
| ACH-2 (USA–ChRL): najmniej obalona H2 (przedłużenie krótkie, „bez rozwiązania ziem rzadkich”), H3 (eskalacja) — najwięcej dowodów niezgodnych | Q-0011 = 0.75 (H1+H2+H4); P(brak przedłużenia) ≈ 0.25; Q-0021 = 0.683 | **w większości spójne**. Napięcie: jeśli H2 oznacza „bez rozwiązania ziem rzadkich”, to Q-0021 (przedłużenie zawieszenia kontroli) mogłoby być niższe. Ale nieprzedłużenie zawieszenia przy przedłużonym rozejmie oznaczałoby powrót kontroli z 09.10.2025, czyli eskalację sprzeczną z H2. „Bez rozwiązania” rozumiem jako brak porozumienia o licencjach — bez korekty. |
| ACH-3 (wojska USA): najmniej obalone H1 i H2 (obie z redukcją w Europie); H3 osłabiona | Q-0003 = 0.333 implikowało przewagę H3 | **niespójne** → korekta Q-0003 +0.07 (§3) |
| W16/Z8: impas z powolnym postępem RU | Q-0004 = 0.227; Q-0073 = 0.117 | spójne |
| Z4 (Rosja poniżej progu ofiar na terytorium NATO) | Q-0002 = 0.06; Q-0027 = 0.113 | spójne |
| Z6 (UE bez fizycznego niedoboru; kruche dla DE) | Q-0010 = 0.35; Q-0009 = 0.30 | spójne |

---

## 6. Podsumowanie

- Korekty: 9 z 73 pytań (+0.12, +0.10, +0.10, +0.08, +0.07, +0.05, +0.01, −0.05, −0.07); żadna nie przekracza ±0.15. Typy: dowód — 5 (Q-0054, Q-0040, Q-0003 z elementem spójności, Q-0039, Q-0050), logika — 3 (Q-0062, Q-0031, Q-0002), mieszany logika + dowód — 1 (Q-0013).
- Rozrzut > 0.30: 1 pytanie (Q-0040) — przewaga soczewki B.
- Skrzywienie kierunkowe: niewykrywalne przy obecnej liczbie pytań; KOMPROMIS wysoko z powodu konstrukcji SQ dla przedłużeń.
- Największe ryzyko nieobjęte korektami: skorelowany błąd założenia Z1 („hamulec wyborczy”) w ok. 10 pytaniach (§1 p. 1) i pominięcie Izraela (§1 p. 2).
