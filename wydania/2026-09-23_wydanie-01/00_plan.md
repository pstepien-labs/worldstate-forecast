# Wydanie 01 — plan (etap 00)

## 1. Parametry wydania

| Parametr | Wartość |
|---|---|
| NR | 01 |
| DATA_STANU | 23.09.2026 |
| OKRES_OD | 21.09.2026 (data stanu wydania 00) |
| KATALOG | `wydania/2026-09-23_wydanie-01` |
| POPRZEDNIE | `wydania/2026-09-21_wydanie-00` (punkt wyjścia, nierozliczane) |
| Metodologia | v1.0 (zamrożona) |
| Następne wydanie (orientacyjnie, +14 dni) | ok. 07.10.2026 — do potwierdzenia przez użytkownika |

**Uwaga o okresie.** README planował wydanie 01 na 05.10.2026; wydanie uruchomiono z DATA_STANU 23.09.2026, więc okres badany ma tylko 2 dni (21–23.09). Etap 02 powinien więc (a) zweryfikować obraz z wydania 00, który w całości „wymaga weryfikacji” (stan_00.md), i (b) wyłapać zmiany z 21–23.09. Horyzont „do następnego wydania” (metodologia §3.3) liczony jest od DATA_STANU: przy rytmie 14 dni termin tych pytań to ok. 07.10.2026.

## 2. Pytania do rozstrzygnięcia w etapie 01

**Brak.** `rejestr/pytania.csv` zawiera tylko nagłówek (0 pytań), więc nie ma pytań AKTYWNYCH z terminem ≤ 23.09.2026 ani takich, w których zdarzenie mogło już zajść. Etap 01 tworzy `01_rozstrzygniecia.md` i `01_wyniki.md` z adnotacją „brak rozstrzygnięć w tym wydaniu”.

Propozycje z wydania 00 (`rejestr/pytania_propozycje_z_wydania_00.csv`, 28 wierszy, status PROPOZYCJA) nie są pytaniami rejestru i nie podlegają rozstrzyganiu. Sygnały istotne dla etapu 03 (przyjęcie propozycji do panelu):

- **P-026** (deficyt w projekcie budżetu Rosji na 2027 r. > 2,0% PKB, termin 31.10.2026). 21.09.2026 Siłuanow na Moskiewskim Forum Finansowym podał deficyt „około 2% PKB” (Wiedomosti, 21.09.2026, https://www.vedomosti.ru/economics/news/2026/09/21/1230540-federalnii-byudzhet-2027). Próg 2,0% leży dokładnie na zapowiadanej wartości, a projekt wpłynie do Dumy prawdopodobnie przed 01.10. OCENA: jeśli projekt wpłynie przed etapem 03, pytanie nie spełni wymogu §3.2 („zdarzenie możliwe do zajścia po dacie utworzenia”) — etap 03 musi to sprawdzić i w razie potrzeby przeformułować (np. na ustawę przyjętą w III czytaniu).
- **P-005** (trójstronne spotkanie USA–UA–RU do 30.11). Witkoff mówił o „ruchu w sprawie wyznaczenia kolejnych rozmów trójstronnych” (The Hill, IX 2026); daty nie znaleziono.
- **P-006** (dekret o mobilizacji / rezerwistach). Pobór w 2026 r. jest całoroczny (dekret nr 998 z 29.12.2025, 261 tys. osób; wysyłka do jednostek 01.10–31.12 — Garant.ru). Osobny „dekret o jesiennym poborze” nie jest więc spodziewany; założenie z K.6 wydania 00 („jesienny pobór … ewentualny dekret”) wymaga korekty w etapie 03.
- **P-018/P-019** (wojska USA w PL). 18.09.2026 Trump zapowiedział bliskie porozumienie o nowej stałej bazie w Polsce, a Pentagon rozważa wycofanie ok. 25 tys. żołnierzy z innych państw Europy; dodatkowe 5 tys. dla PL jeszcze nie zrealizowane (Stars and Stripes, 18.09.2026).

## 3. Kalendarz 23.09–04.11.2026 (6 tygodni)

Status: **P** = potwierdzone w sieci w etapie 00; **N** = niepotwierdzone (sprawdzić w etapie 02).

| Data | Wydarzenie | PIR | Status | Źródło |
|---|---|---|---|---|
| 23–25.09 | Wizyta państwowa Xi Jinpinga w USA; ceremonia i szczyt w Białym Domu 24.09. Na stole: cła, ziemie rzadkie (termin 10.11), Tajwan (pakiet 14 mld USD), Iran, AI | PIR-4, PIR-5 | P | whitehouse.gov (komunikat Pierwszej Damy, IX 2026); SCMP (potwierdzenie Pekinu); Bloomberg 22.09.2026 |
| tydzień 22.09 | Debata generalna ZO ONZ w Nowym Jorku; delegacja Iranu „z pełnomocnictwem” do wznowienia dyplomacji | PIR-5 | P | US News/Reuters 22.09.2026 |
| do ok. 25.09 | Ostateczne wyniki wyborów do Dumy (CKW) | PIR-7 | P (termin przybliżony) | Al Jazeera 21.09.2026 |
| 30.09 / 01.10 | Koniec roku budżetowego USA — shutdown **nie** grozi: CR do 11.12.2026 przyjęty (Senat 90–6, Izba 370–48) | PIR-6 | P | NPR 01.09.2026; NBC News |
| do 01.10 | Wniesienie do Dumy projektu budżetu Rosji na 2027–2029 (Siłuanow: deficyt 2027 ok. 2% PKB) | PIR-1, PIR-6 | N (data wniesienia) | Wiedomosti 21.09.2026 |
| 01.10 | Początek jesiennej wysyłki poborowych w Rosji (pobór całoroczny, 261 tys. w 2026 r.) | PIR-1 | P | Garant.ru (dekret nr 998 z 29.12.2025); kremlin.ru/acts/news/78905 |
| 03.10 | Wybory parlamentarne na Łotwie | PIR-7 | P | Wikipedia (indeks) — potwierdzić w CVK Łotwy |
| 04.10 | Wybory powszechne w Brazylii (II tura 25.10) | PIR-7 | P | AS/COA |
| 04.10 | Wybory powszechne w Bośni i Hercegowinie | PIR-7 | P | Model Diplomat — potwierdzić w CIK BiH |
| 06–07.10 | Posiedzenie RPP (decyzja 07.10, projekcja inflacyjna) | PIR-6 | P | PAP Biznes (harmonogram NBP na 2026) |
| do 08.10 | Ćwiczenia „Namejs 26” na Łotwie (ok. 12 tys. żołnierzy, od 02.09) | PIR-1, PIR-2 | P | grosswald.org (jedno źródło — potwierdzić) |
| X (bez daty) | Trójstronne rozmowy USA–UA–RU (wydanie 00: ZEA, „co do zasady”) | PIR-1, PIR-7 | N | The Hill (brak daty) |
| X (bez daty) | Posiedzenie JMMC OPEC+ | PIR-3 | N | tradingnewsterminal (bez daty) |
| X (ok. połowy miesiąca) | Raport miesięczny IEA (Oil Market Report) | PIR-3 | N | — |
| 12–18.10 | Doroczne zgromadzenie MFW i Banku Światowego, Bangkok (plenarne 16.10) | PIR-6 | P | imf.org |
| 15–16.10 | Rada Europejska, Bruksela | PIR-2, PIR-3, PIR-6 | P | consilium.europa.eu; brussels.be |
| 23.10 | Posiedzenie Banku Rosji (stopa kluczowa obecnie 14,00%) | PIR-6 | P | cbr.ru (kalendarz decyzji) |
| 25.10 | II tura wyborów w Brazylii (jeśli potrzebna) | PIR-7 | P | AS/COA |
| 27–28.10 | FOMC (decyzja 28.10, SEP) | PIR-6 | P | federalreserve.gov; FedRateCalc |
| 29.10 | Posiedzenie EBC w sprawie polityki pieniężnej | PIR-6 | P | ECB (kalendarz posiedzeń) za Young Platform/IG |
| 03.11 | Wybory połówkowe w USA | PIR-2, PIR-7 | P (wydanie 00) | stan_00.md; potwierdzić w G4 |
| 03–04.11 | Posiedzenie RPP (decyzja 04.11) | PIR-6 | P | PAP Biznes |
| pocz. XI | Wygaśnięcie przedłużonej siły wyższej w Katarze (Ras Laffan) | PIR-3 | N | wydanie 00, sekcja J (jedno źródło) |

Tuż za oknem: 10.11 — wygasa zawieszenie chińskich kontroli ziem rzadkich; 18–19.11 — APEC w Shenzhen; 11.12 — wygasa CR w USA; XII — G20 na Florydzie.

Nie znaleziono: posiedzenia ministrów obrony NATO w X 2026 (w 2026 r. dotąd 12.02 i 18.06 — nato.int). Sprawdzić w G1.

## 4. PIR (bez zmian, metodologia v1.0 §2)

- **PIR-1** Zdolność i wola Rosji do eskalacji wobec NATO i wschodniej flanki.
- **PIR-2** Zdolność i wola USA/NATO do reakcji; obecność USA w Europie i w Polsce.
- **PIR-3** Ceny i dostępność energii (ropa, gaz, paliwa) w Europie i w Polsce.
- **PIR-4** Rywalizacja USA–Chiny: handel, technologie, surowce, Tajwan.
- **PIR-5** Wojna z Iranem i szlaki morskie (Ormuz, Bab al-Mandab, Suez).
- **PIR-6** Kondycja finansowa mocarstw i warunki kapitałowe, w tym PLN.
- **PIR-7** Przesunięcia orientacji państw (wybory, sojusze, zmiany władzy).

## 5. Przegląd nagłówków (15 zapytań) — co się ruszyło

Sygnały z nagłówków, nie rekordy faktów. Każdy wymaga weryfikacji i trzech perspektyw w etapie 02.

| Wektor / region | Sygnał (data, źródło) | Zmiana vs wydanie 00 |
|---|---|---|
| MIL/DYP — Iran, Ormuz | 20–21.09: dowództwo centralne sił zbrojnych Iranu twierdzi, że USA „przy wsparciu państw regionu” przygotowują wznowienie uderzeń; grozi odwetem na bazach USA (Al Jazeera 21.09; Al Arabiya 20.09; Times of Israel). 22.09: wysoki rangą urzędnik Iranu (Reuters za US News, CNBC): Ormuz może zostać otwarty w 7 dni, jeśli USA zniosą blokadę i ogłoszą drogę dyplomatyczną; Ghalibaf — Ormuz zamknięty do spełnienia zobowiązań USA. Mediatorzy: Katar, Pakistan | **Duża.** Dwutorowy sygnał: ryzyko wznowienia wojny i jednocześnie oferta otwarcia Ormuzu. Tego nie było w wydaniu 00 |
| DYP/GOS/FIN — USA–Chiny | Szczyt 24.09. 18.09 Trump podpisał „Sanctioning Russia and Iran Act”: cła do 100% na największych importerów rosyjskiej ropy i gazu (w tym Chiny), przedłużenie Iran Sanctions Act o 5 lat (za CFR/Bloomberg, 21–22.09 — źródło pierwotne do ustalenia) | **Duża.** Nowe narzędzie sankcyjne tuż przed szczytem; wydanie 00 go nie znało |
| ENE — ropa | Brent ok. 99–100 USD 22.09 (Fortune; Investing, zakres dnia 99,58–102,29) | Spadek z ~104 USD (19.09) — możliwa reakcja na sygnały z Iranu; zweryfikować zamknięcia |
| ENE — gaz | TTF ok. 78–81 EUR/MWh (16.09), szczyt ~84 na pocz. IX; magazyny UE 68,49% (15.09) vs średnia 5-letnia 84% (IndexBox; EnergyRiskIQ) | Bez zmian — potwierdzenie obrazu z 00; brak danych po 16.09 |
| INF — Bab al-Mandab | Huti kontrolują całe wybrzeże Morza Czerwonego, Perim (11.09) i wyspy Hanisz; blokada statków saudyjskich; >300 zabitych w walkach (Al Jazeera 11.09; Washington Post 10.09; Times of Israel — saudyjskie uderzenie na więzienie) | Potwierdzenie z pogłębieniem: „ogr.” w bloku L może być za słabe — sprawdzić przepływy |
| WEW — Rosja | Wybory do Dumy 18–20.09: Jedna Rosja 57,83% (95% protokołów), ok. 355/450 mandatów, frekwencja 56,7%; Sprawiedliwa Rosja poniżej 5% (Al Jazeera, Moscow Times 21.09) | **Zamknięta luka** z sekcji J wydania 00 (wyniki cząstkowe) |
| FIN — Rosja | Siłuanow 21.09: deficyt 2027 „około 2% PKB”, „bez ryzyk” (Wiedomosti) | Nowe; kluczowe dla P-026 |
| MIL — Ukraina/Rosja | 19/20.09 największy ukraiński pakiet rakiet i dronów na obwód moskiewski; Rosja buduje podziemne zakłady dronów w Ałabudze (ISW 21.09 za Kyiv Post) | Zmiana akcentu: presja UA na głębię Rosji; front — brak nowych danych |
| DYP — Ukraina | Rozmowy Witkoff–Kushner z Putinem (05.09) i Zełenskim (06–07.09); „ruch w sprawie kolejnych rozmów trójstronnych” (The Hill), bez daty | Bez zmian wobec 00 |
| MIL — USA w Europie i PL | 18.09: Trump — bliskie porozumienie o nowej stałej bazie armii USA w Polsce; Pentagon rozważa wycofanie ok. 25 tys. z Europy (NBC: „prawie jedna trzecia”); obecnie ok. 80 tys.; NDAA 2026 §1249 — próg 76 tys. na środkach FY2026 (Stars and Stripes 18.09; The National 18.09; NBC) | **Duża.** Nowe liczby przeglądu postawy sił; rozjazd „mniej w Europie / więcej w PL” |
| MIL — flanka | Wynik wyszukiwania zawierał zdanie o „prawie dwóch tuzinach dronów nad Polską 10.09” — najpewniej dotyczy 10.09.2025, nie 2026. Nie przyjmuję | Brak nowego incydentu 21–23.09 w nagłówkach — sprawdzić w G1 |
| MIL — Sahel | 14.09 atak JNIM na bazę lotniczą w Sévaré; 19.09 atak na punkt kontrolny pod Bamako; 20.09 narada kryzysowa u Goïty; blokada paliwowa stolicy (Al Jazeera 22.09; Rio Times) | Pogorszenie względem 00 |
| MIL — Tajwan | Brak nazwanych ćwiczeń PLA wokół Tajwanu w IX 2026 w wynikach; od VII regularne patrole straży przybrzeżnej ChRL na wschód od Tajwanu (The Diplomat, IX 2026) | Bez dużej zmiany; luka w danych |

## 6. Priorytety zbierania (etap 02)

Zasada ogólna: okres 21–23.09 jest krótki, więc każda grupa **najpierw weryfikuje wartości bloku L z wydania 00** (każda z datą i źródłem), potem szuka zmian. Zdarzenia oznaczone ★ są kluczowe (trzy perspektywy Z/A/T).

**G1 — MIL + INF**
1. ★ Iran: groźba wznowienia uderzeń USA (20–21.09) i oferta otwarcia Ormuzu (22.09) — perspektywy: USA (CENTCOM, Pentagon), Iran (FA: IRNA, Tasnim, oświadczenie Chatam al-Anbija), strona trzecia (Katar, Pakistan, Oman; AR). Przepływy przez Ormuz wg IMF PortWatch po 13.09.
2. ★ Bab al-Mandab: skala blokady Huti, uderzenia saudyjskie, przepływy przez cieśninę i Suez; status „ogr.” vs „zamknięty dla części bander”.
3. ★ USA w Europie i PL: liczby przeglądu postawy sił, baza stała w PL, stan realizacji +5 tys.; §1249 NDAA po 30.09 (CR do 11.12 — czy przedłuża ograniczenie?).
4. Flanka: incydenty 21.09–23.09, ostatni art. 4 (luka z 00), Namejs 26.
5. Ukraina: linia frontu (ISW; ilościowo km²), uderzenia na głębię Rosji.
6. Tajwan/MPŁ: aktywność PLA, lotniskowce USA w Indo-Pacyfiku (stan na IX — w 00 niepotwierdzony).

**G2 — ENE + TEC**
1. ★ Brent (zamknięcia 19–23.09) i reakcja na sygnały z Iranu; raport IEA z IX.
2. ★ TTF i magazyny UE/PL po 15.09; Katar (Ras Laffan, siła wyższa do pocz. XI — w 00 jedno źródło).
3. Rurociąg saudyjski Wschód–Zachód (wyłączony 11.09) — status.
4. Paliwa w PL: cena diesla, mechanizm cen maksymalnych (sprzeczność z 00).
5. ★ Ziemie rzadkie: wyniki szczytu 24.09 dla terminu 10.11 (MOFCOM, Xinhua; perspektywa T — Japonia/UE).

**G3 — GOS + FIN**
1. ★ „Sanctioning Russia and Iran Act” (18.09): tekst, podstawa prawna, terminy wejścia w życie ceł; reakcja MSZ/MOFCOM ChRL i Indii.
2. ★ Szczyt USA–Chiny 24.09: cła, przedłużenie rozejmu celnego (termin 10.11).
3. Budżet Rosji 2027–2029: data wniesienia do Dumy, deficyt, wydatki obronne; stopa Banku Rosji (14,00%).
4. Stopy: EBC 2,50%, NBP 3,75%, Fed — potwierdzić; EUR/PLN (luka z 00); deficyt Polski 2026 (luka z 00).
5. Sankcje UE wobec Rosji — stan prac nad kolejnym pakietem; finansowanie Ukrainy i SAFE.

**G4 — DYP + WEW**
1. ★ Iran–USA dyplomacja w tygodniu ZO ONZ (mediatorzy Katar, Pakistan); status Modżtaby Chameneiego.
2. ★ Rozmowy o Ukrainie: data rozmów trójstronnych; stanowiska Kremla (Uszakow, Pieskow) i Kijowa.
3. Rosja po wyborach do Dumy: ostateczne wyniki CKW, skład, zmiany kadrowe.
4. Wybory 03–04.10: Łotwa, Brazylia, BiH; wybory połówkowe w USA — stan kampanii.
5. Sahel (Mali — oblężenie Bamako), Wenezuela (termin wyborów), Kaukaz, Grenlandia — po jednej weryfikacji statusu.

## 7. Problemy z rejestrem (kontrola integralności)

| Kontrola | Wynik |
|---|---|
| Kodowanie i BOM | Wszystkie 6 plików CSV w `rejestr/`: UTF-8 z BOM, separator `;` — OK |
| Nagłówki vs szablon | Nagłówki `pytania.csv`, `prognozy.csv`, `benchmarki.csv`, `rozstrzygniecia.csv`, `zrodla.csv` zgodne z pakietem startowym i z kolumnami czytanymi przez `narzedzia/wyniki.py` — OK |
| Liczba wierszy | `pytania`, `prognozy`, `benchmarki`, `rozstrzygniecia`, `zrodla`: tylko nagłówek (0 wierszy danych) |
| Unikalne ID pytań | Nie dotyczy (0 pytań). W pliku propozycji: 28 ID (P-001…P-028), wszystkie unikalne, 17 pól w każdym wierszu |
| Prognozy do nieistniejących pytań | Brak (0 prognoz) |
| Zmiany w historii | Brak poprzedniego tagu git — repozytorium zainicjowane w tym etapie (commit „stan początkowy”). Porównanie możliwe od wydania 02 |
| Uwagi | (1) `rejestr/zrodla.csv` jest pusty — etap 02 musi dopisywać źródła. (2) Propozycje z 00 mają `p_status_quo` ustalone przed metodologią v1.0 — etap 03 powinien je sprawdzić wg §3.5. |

## 8. Braki etapu 00

- Nie potwierdzono dat: wniesienia budżetu Rosji do Dumy, JMMC OPEC+, raportu IEA z X, rozmów trójstronnych, siły wyższej w Katarze, posiedzenia ministrów obrony NATO w X.
- Wybory na Łotwie potwierdzone tylko przez indeks (Wikipedia) — wymaga źródła pierwotnego (CVK).
- Źródło pierwotne „Sanctioning Russia and Iran Act” (Congress.gov / whitehouse.gov) nie zostało otwarte.
