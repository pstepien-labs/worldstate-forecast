# Etap 08 — Kontrola jakości i zamknięcie wydania 01

Data kontroli: 24.09.2026 · Data stanu wydania: 23.09.2026 · Katalog: `wydania/2026-09-23_wydanie-01`

Zakres poprawek: wyłącznie `07_raport.md` i `07_blok_stanu.md`. Prognoz, rejestru, plików 02–06 nie zmieniano — niezgodności w nich są tylko zapisane.

## Podsumowanie

| # | Punkt kontrolny | Wynik |
|---|---|---|
| 1 | Fakty (kompletność zapisu, próba 15 URL-i) | **Niezgodność** — 2 z 15 rekordów niezgodne ze źródłem, 1 potwierdzony częściowo; rekordy z etapu 04 skrócone (poprawiono raport) |
| 2 | Rozdział fakt / ocena / prognoza | **Niezgodność (poprawiona)** — liczby poza sekcją H: blok L (55%), sekcja J.5 (+0.01) |
| 3 | Kompletność prognoz | **OK** — 73/73 pytań z A, B, C, AGR, AGR_RT |
| 4 | Rejestr tylko do dopisywania | **OK** — wyłącznie dopisane wiersze |
| 5 | Ślepota | **OK z zastrzeżeniami** — 2 zgłoszone przypadkowe ekspozycje (04-B, 04-C); brak odwołań do benchmarków i domen zakazanych |
| 6 | Bank pytań | **OK** — horyzonty 38/44/18%, trywialność 1,4%, 8/8 wektorów, panel 40 |
| 7 | Perspektywy źródeł | **Niezgodność (brak treści do poprawienia w rekordach)** — trzy perspektywy dla 15 z 24 zdarzeń kluczowych (63%); J.3 uzupełniona |
| 8 | Dziennik | **Niezgodność (uzupełniona tutaj)** — brak godzin etapów w dzienniku; brak zgłoszeń prób wstrzyknięcia poleceń |

## 1. Fakty

**Kompletność zapisu w raporcie.** Fakty w sekcjach A–J odwołują się do rekordów `02_fakty/G*.md` (213 rekordów, każdy z 13 polami: data, aktor, działanie, adresat, wektor, region, status, wydawca, URL, ocena A–F/1–6, perspektywa, PIR — sprawdzone mechanicznie, brak pustych pól). Niezgodności:

- Fakty dociągnięte w etapie 04 (A-dod., B-dod., C-01…C-14) mają rekord skrócony: data, wydawca, URL — bez oceny źródła, perspektywy i PIR. „A-dod.” i „B-dod.” nie mają numerów, więc odwołanie w raporcie nie wskazuje jednego rekordu. **Poprawka w raporcie:** dopisek w „Konwencji oznaczeń”. Rekordów w plikach 04 nie zmieniano.
- Kilka faktów w sekcji K pochodzi z `00_plan.md`, nie z rekordu G (np. dekret nr 998 o poborze — Garant.ru, kremlin.ru). Mają źródło i URL w `00_plan.md`, ale nie mają oceny źródła. Bez poprawki; do wydania 02: przenosić takie fakty do rekordów G.

**Próba 15 faktów.** Populacja: 171 identyfikatorów rekordów (G1–G4, C-xx) przywołanych w tekście głównym raportu. Losowanie: `random.seed(1)` (Python), `random.sample(sorted(ids), 15)`. Polecenie jednorazowe, bez pliku w repozytorium.

| Rekord | Sprawdzony URL | Wynik | Uwagi |
|---|---|---|---|
| C-12 | energyriskiq.com/gas-storage-levels-in-europe | **Niezgodność** | Źródło: ok. 5,6 TWh/d potrzebne do celu **90%** na 01.11, nie 80%. Błąd znany (05 §1 p. 9); raport opisuje go w J.5 |
| G1-007 | iranintl.com (za Kyodo) | Potwierdzony | Oferta 7 dni, przekazanie 16.09, wykluczone spotkanie Pezeszkian–Trump. US News — przekroczony czas pobierania |
| G1-018 | globalsecurity.org (oprep) | Częściowo | Strona (aktualizowana codziennie) podaje „decyzję z 19.09 o nieuderzaniu w Huti”. Ponownej prośby następcy tronu nie potwierdzono — pochodzi z CNN, niedostępnego już w etapie 02 (ocena C/3 adekwatna) |
| G1-025 | stripes.com | Potwierdzony | „Major progress”, lokalizacja „very soon”; brak informacji o stałym stacjonowaniu |
| G1-030 | anews.com.tr (NBC — tylko fragment) | Potwierdzony | 25–40 tys. z ok. 80 tys., możliwe przesunięcie na flankę, rekomendacja 06.11 |
| G1-059 | windward.ai | Potwierdzony | 1–2 mln USD za statek za rejs; artykuł z 09.09.2026 |
| G2-011 | rigzone.com | Potwierdzony z uwagą | Utrzymanie produkcji w X, kwota saudyjska 10,478 mln b/d, spotkanie 04.10 — potwierdzone. „Zakończenie wycofania 1,65 mln b/d we IX” — nie w tym źródle (element rekordu nieużyty w raporcie) |
| G3-006 | theweek.in | Potwierdzony z uwagą | Treść stanowiska MSZ Indii potwierdzona; nazwisko rzecznika (Jaiswal) nie pada w tym artykule |
| G3-010 | china-briefing.com | Potwierdzony | 12,5% z s.301 od 24.07.2026, wyrok SN z 20.02.2026, średnia 36,8% → 29,7% |
| G3-028 | chinanews.com.cn | Potwierdzony z uwagą | LPR 3,0% i 3,5%, 20.09.2026; artykuł nie mówi wprost „bez zmian” |
| G3-035 | euronews.com | Potwierdzony z uwagą | 36 miesięcy, delisting Usmanowa i Fridmana, wstrzymanie się Łotwy. Liczba objętych: Euronews „ponad 2600”, rekord „ok. 3000” (liczba nieużyta w raporcie) |
| G3-040 | eurointegration.com.ua; globalsecurity.org (gov.ua) | Potwierdzony | 32,6 mld USD luki 2027, ok. 50 mld USD/rok, „koncepcja, nie gotowy plan” |
| G3-043 | tariffstool.com | Potwierdzony | Pułap 15% z MFN od 01.07.2026, auta 15%, stal i aluminium 50% |
| G4-020 | aljazeera.com | Potwierdzony | Twierdzenie Trumpa o rozejmie energetycznym, uderzenia wznowione niemal natychmiast |
| G4-049 | armenianweekly.com; cacianalyst.org | **Niezgodność** | Traktat niepodpisany i warunek konstytucyjny — potwierdzone. **„Referendum w 2027” — brak w obu źródłach** (CACI: referendum „bez ustalonego terminu”; artykuł CACI z 15.01.2026) |

Wynik: 12 z 15 potwierdzonych (w tym 4 z drobnymi uwagami do elementów rekordu nieużytych w raporcie), 1 częściowo, 2 niezgodne. **Poprawki w raporcie:** G4-049 — sekcja E (wiersz Armenia–Azerbejdżan, także OCENA „zablokowany do 2027 r.”) i blok L („Kaukaz”); to samo w `07_blok_stanu.md`. C-12 — raport opisuje błąd już w J.5, bez zmian.

Niezgodność bez poprawki: uzasadnienia prognoz Q-0072 w plikach 04 mogą opierać się na „referendum 2027”. Prognoz się nie zmienia — do uwzględnienia przez soczewki w wydaniu 02.

## 2. Rozdział fakt / ocena / prognoza

Przeszukano tekst poza sekcją H i aneksem pod kątem wartości 0.xx i procentów przy słowach „prawdopodob…”/„szans…”. Znalezione:

- Blok L (raport, linia `scenariusz_bazowy`) i `07_blok_stanu.md`: „55%”. Liczbowe prawdopodobieństwo poza sekcją H (CLAUDE.md p. 3.1; format wydania 00 nie zawierał liczby). **Poprawione** na odesłanie do H.1.
- J.5: „(+0.01)” — wielkość korekty red teamu. **Poprawione** na odesłanie do aneksu.
- Konwencja (skala słowna z §10) i procentowe zmiany cen (np. Brent −4–5%) — to nie prognozy, bez zmian.

Spójność skali słownej: H.1 opisywała 55% jako „prawdopodobny”, a aneks przyjmuje, że 0.45–0.55 włącznie to „równe szanse”. **Poprawione** na „mniej więcej równe szanse (najbardziej prawdopodobny z trzech)”.

Zgodność liczb z rejestrem: 73 wiersze aneksu — AGR_RT, A/B/C, rozrzut, pewność, treść pytania i termin zgodne z `rejestr/prognozy.csv` i `pytania.csv`. W rejestrze p ma 3 miejsca po przecinku, w raporcie 2. Wszystkie różnice ≤ 0.005, czyli tylko zaokrąglenia. Liczby w H.1–H.3 zgodne. Statystyki H.3 (średnia 0.338, przedziały 23/28/11/8/3, pewność 50/23, trywialność 1/73) potwierdzone przeliczeniem.

## 3. Kompletność prognoz

73 pytania AKTYWNE; dla każdego w wydaniu 01 jest dokładnie jeden wiersz A, B, C, AGR i AGR_RT (365 wierszy). AGR = średnia A, B, C (różnice ≤ 0.005). AGR_RT ≠ AGR dla 9 pytań, zgodnie z korektami przyjętymi w 06 (Q-0002 +0.01, Q-0003 +0.07, Q-0013 +0.10, Q-0031 −0.05, Q-0039 −0.07, Q-0040 +0.10, Q-0050 +0.05, Q-0054 +0.12, Q-0062 +0.08; wszystkie w limicie ±0.15). Wszystkie p w przedziale 0.01–0.99. **OK.**

## 4. Rejestr tylko do dopisywania

Tag poprzedniego wydania nie istnieje — repozytorium powstało na starcie wydania 01. Punkt odniesienia: commit `cd7a7bd` („stan początkowy”, nagłówki rejestru).

| Plik | Dodane | Usunięte lub zmienione |
|---|---|---|
| prognozy.csv | 365 | 0 |
| benchmarki.csv | 43 | 0 |
| rozstrzygniecia.csv | 0 | 0 |
| pytania.csv | 73 | 0 |
| zrodla.csv | 186 | 0 |

Sprawdzono też każdy commit osobno (`git diff <c>~1 <c> -- rejestr/`): w żadnym nie usunięto ani nie zmieniono wiersza. `benchmarki.csv` zmienił się tylko w commicie etapu 06 (3d9c888), który powstał po commicie „prognozy zamrożone” (32a635e). **OK.** Od wydania 02 punktem odniesienia będzie tag `wydanie-01`.

## 5. Ślepota

- Pliki 03, 04_A/B/C, 05 przeszukano pod kątem nazw serwisów prognostycznych (lista CLAUDE.md p. 9, a także robinhood, octagonai, natesilver, racetothewh), słów „odds”, „prediction”, „rynek predykcyjny” i „benchmark” oraz odwołań do plików `06_*` i `07_zalacznik*`. Trafienia dotyczą tylko deklaracji, że tych plików nie otwierano, i zgłoszenia linku robinhood.com w wynikach wyszukiwania (04-A; linku nie otwarto).
- Historia git: `06_agregacja.md` powstał w commicie zamrożenia, `06_benchmarki.md` w etapie 06, `07_zalacznik_benchmarki.md` w etapie 07 — wszystkie po etapach 03–05.
- Historii sesji etapów 03–05 nie da się sprawdzić z tej sesji. Kontrola opiera się na plikach i dzienniku.
- Zgłoszone ekspozycje (dziennik): 04-B zobaczyła 2 wiersze soczewki A (Q-0001, Q-0002) z wartościami p. 04-C zobaczyła fragment uzasadnienia B (Q-0073, bez p) i wpisy dziennika 04-A/04-B po zapisaniu swoich prognoz. Obie opisane w raporcie J.5. Ryzyko strukturalne: dziennik wydania, czytany przez kolejne soczewki, zawiera tematy wyszukiwań i zakresy p innych soczewek. **Wniosek procesowy (do akceptacji użytkownika):** wpisy 04 w dzienniku bez zakresów p, a soczewki nie czytają wpisów 04 innych soczewek.

Wynik: **OK z zastrzeżeniami** (ekspozycje przypadkowe, zgłoszone, bez odwołań do benchmarków).

## 6. Bank pytań

| Wymóg | Stan | Wynik |
|---|---|---|
| Horyzonty (§3.3: ok. 40/40/20) | do 10.10.2026: 28 (38%); do 31.12.2026: 32 (44%); dłuższe: 13 (18%) | OK |
| Trywialność (§3.8: ≤ 20% poza 0.05–0.95) | 1/73 (1,4%) — Q-0001 (0.03) | OK |
| Pokrycie 8 wektorów | MIL 15, FIN 12, ENE 10, DYP 9, WEW 8, GOS 7, INF 7, TEC 5 | OK |
| Panel (40, po 5 na wektor) | 40; po 5 w każdym z 8 wektorów | OK |
| Pytania swobodne (20–40) | 33 | OK |
| Kompletność pól | kryterium, źródło rozstrzygnięcia, klaster — wszystkie wypełnione; brak duplikatów treści | OK |

Obserwacje (nie niezgodności): p_status_quo = 0.10 w 65 z 73 pytań (0.50 — 6, 0.90 — 2), więc punkt odniesienia status quo będzie niemal jednolity. czyj_sukces = BRAK w 58 z 73 pytań, więc błąd kierunkowy da się liczyć na 15 pytaniach (KOMPROMIS 7, ROSJA 3, UKRAINA 2, UE, CHINY, USA_ZACHOD po 1).

## 7. Perspektywy źródeł

**Fakty według perspektywy** (213 rekordów G1–G4; rekord może mieć kilka perspektyw):

| Perspektywa | Rekordy z tą perspektywą | Udział | Tylko ta perspektywa |
|---|---|---|---|
| Z | 118 | 55% | 76 (36%) |
| A | 83 | 39% | 54 (25%) |
| T | 66 | 31% | 34 (16%) |
| Więcej niż jedna | — | — | 49 (23%) |

Rozkład w grupach: G1 najbardziej zachodni (Z 43, A 19, T 14); G4 najbardziej zrównoważony (A 29, T 26, Z 25).

**Zdarzenia kluczowe z trzema perspektywami: 15 z 24 (63%).**

- Komplet (15): oferta Iranu i Ormuz; atak Huti na Rijad; wojska USA w PL; kolizja CCG–BFAR; ropa i rurociąg Wschód–Zachód; ziemie rzadkie; H.R. 5334; przygotowanie szczytu USA–ChRL; sankcje UE (36 mies.); waluty i płatności; rozmowy Iran–USA; rozmowy o Ukrainie; Grenlandia; Mali; Wenezuela.
- Brak (9): incydenty bałtyckie (brak T i RU/BY); front w Ukrainie (T); Tajwan (A — ChRL); KRLD (A, T); Katar LNG (T); rafinerie w Rosji (T); budżet Rosji 2027 (Z); rating Polski (T); wybory do Dumy (T).

**Poprawka w raporcie:** tabela J.3 nie wymieniała 4 zdarzeń z lukami (Katar LNG, rafinerie, budżet RU, rating PL) — dopisano je. Do wydania 02: T dla frontu i incydentów bałtyckich to luki powtarzalne; zrodla/mapa_zrodel.md powinna wskazywać źródła T dla PIR-1.

## 8. Dziennik

- **Czasy etapów** — dziennik nie podaje godzin (poza startem 00 o 00:14). Uzupełnienie z historii git (czasy commitów, 23.09.2026):

| Etap | Commit | Godzina |
|---|---|---|
| 00 | cbe7e4f | 00:18 |
| 01 | e643392 | 00:20 |
| 02-G1 / G2 | f669846 / 4bc0e21 | 00:35 / 00:50 |
| 02-G3 (2 sesje) | 0a5826c | 09:41 |
| 02-G4 | 5b7b7ef | 10:27 |
| 03 (+ korekta dziennika) | 9e78c4c, c97c33f | 22:03–22:04 |
| 04-A / 04-B / 04-C | 506cf77 / a643929 / bac8b26 | 22:14 / 22:23 / 22:43 |
| 05 | 59462d4 | 23:11 |
| prognozy zamrożone | 32a635e | 23:13 |
| 06 | 3d9c888 | 23:27 |
| 07 | 5bfe42e | 23:44 |
| 08 | — | 24.09.2026 |

- **Przerwane etapy:** 02-G3 wykonano w dwóch sesjach, a druga kontynuowała od braków (zgodnie z p. 10). Innych przerw nie zapisano.
- **Problemy:** niedostępne źródła (Reuters, CNN, Bloomberg, CNBC, USNI, UKMTO, Metaculus i inne), luki „częściowo” w G1–G4 (decyzja użytkownika w 03: kontynuować), brak PDF raportu (brak konwertera), błąd rachunkowy C-12, nierozstrzygnięta wartość 5,13% dla Sprawiedliwej Rosji.
- **Próby wstrzyknięcia poleceń:** w żadnym etapie nie zgłoszono. W etapie 08 również nie znaleziono ich na 18 pobranych stronach (19 prób, 1 przekroczenie czasu — US News).
- **Linki do rynków predykcyjnych w wynikach wyszukiwania** (nieotwierane): 00 (robinhood.com), 02-G1 (polymarket.com, octagonai.co), 02-G4 (racetothewh.com, natesilver.net), 04-A (robinhood.com).

## Poprawki wprowadzone w raporcie (etap 08)

| Plik | Miejsce | Zmiana | Powód |
|---|---|---|---|
| 07_raport.md | Konwencja oznaczeń | Dopisek: rekordy z etapu 04 są skrócone (bez oceny źródła, perspektywy, PIR; A-dod./B-dod. bez numerów) | Pkt 1 |
| 07_raport.md | E, wiersz Armenia–Azerbejdżan | „referendum dopiero w 2027” → referendum bez ustalonej daty; OCENA „zablokowany do 2027 r.” → „do zmiany konstytucji; termin nieustalony” | Pkt 1, G4-049 |
| 07_raport.md, 07_blok_stanu.md | L, `Kaukaz` | „referendum w Armenii 2027” → „data nieustalona” | Pkt 1, G4-049 |
| 07_raport.md, 07_blok_stanu.md | L, `scenariusz_bazowy` | Usunięto „55%”, dodano odesłanie do H.1 | Pkt 2 |
| 07_raport.md | H.1, scenariusz bazowy 6–12 mies. | „prawdopodobny” → „mniej więcej równe szanse (najbardziej prawdopodobny z trzech)” | Pkt 2, spójność skali §10 z aneksem |
| 07_raport.md | J.5 | Usunięto „(+0.01)” | Pkt 2 |
| 07_raport.md | J.3 | Dopisano 4 zdarzenia kluczowe z brakującą perspektywą | Pkt 7 |

## Niezgodności niepoprawiane (tylko zapis)

1. C-12 (04_prognozy_C.md): 5,5 TWh/d przypisane celowi 80% zamiast 90%. Wpływ na prognozę C dla Q-0067 opisał red team.
2. G4-049 (02_fakty/G4.md): „referendum 2027” bez pokrycia w źródłach.
3. Rekordy faktów etapu 04 bez oceny źródła, perspektywy i PIR (niezgodne z CLAUDE.md p. 3.2).
4. Ekspozycje ślepoty 04-B i 04-C (opisane w dzienniku i J.5).
5. Brak godzin etapów w `dziennik.md` (uzupełnione w tym pliku).

## Propozycje procesowe (wymagają akceptacji użytkownika i wpisu do `zmiany_metodologii.md`)

1. Fakty dociągane w etapie 04 zapisywać pełnym rekordem (ocena, perspektywa, PIR) i z numerem (A-01…, B-01…).
2. W dzienniku wpisy 04 bez zakresów p i bez tematów wyszukiwań; soczewki nie czytają wpisów 04 innych soczewek.
3. Każdy wpis dziennika z godziną rozpoczęcia i zakończenia etapu.
