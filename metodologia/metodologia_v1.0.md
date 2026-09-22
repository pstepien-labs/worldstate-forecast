# Metodologia v1.0

Obowiązuje od wydania 01 do przeglądu kwartalnego (ok. 21.12.2026). Zmiany wyłącznie przez przegląd kwartalny (nowy plik `metodologia_v1.1.md`; ten plik zostaje bez zmian).

## 1. Miara sukcesu

- **Miara główna:** wskaźnik umiejętności Briera (BSS) prognozy oficjalnej AGR_RT względem:
  a) mechanicznego punktu odniesienia status quo (`p_status_quo`),
  b) tłumu lub rynku — tylko na pytaniach z benchmarkiem dopasowanym DOKLADNIE.
- **Miary pomocnicze:** kalibracja, błąd kierunkowy, porównanie przebiegów A / B / C / AGR / AGR_RT.

## 2. Pytania decyzyjne (PIR)

- **PIR-1** Zdolność i wola Rosji do eskalacji wobec NATO i wschodniej flanki.
- **PIR-2** Zdolność i wola USA/NATO do reakcji; obecność USA w Europie i w Polsce.
- **PIR-3** Ceny i dostępność energii (ropa, gaz, paliwa) w Europie i w Polsce.
- **PIR-4** Rywalizacja USA–Chiny: handel, technologie, surowce, Tajwan.
- **PIR-5** Wojna z Iranem i szlaki morskie (Ormuz, Bab al-Mandab, Suez).
- **PIR-6** Kondycja finansowa mocarstw i warunki kapitałowe, w tym PLN.
- **PIR-7** Przesunięcia orientacji państw (wybory, sojusze, zmiany władzy).

Rozdzielczość zbierania wynika z PIR. Region bez związku z żadnym PIR dostaje w raporcie jedną linię.

## 3. Bank pytań

**3.1 Typy.**
- *Panel stały:* 40 pytań, po 5 na każdy z 8 wektorów. Ustalany w wydaniu 01, niezmienny do przeglądu kwartalnego. Wyjątek: pytanie rozstrzygnięte zastępuje się nowym z tego samego wektora i klastra.
- *Pytania swobodne:* 20–40 nowych w każdym wydaniu.

**3.2 Wymogi pytania.** Binarne TAK/NIE; jednoznaczne kryterium rozstrzygnięcia; wskazane publiczne źródło rozstrzygnięcia; termin (data); zdarzenie możliwe do zajścia po dacie utworzenia; brak duplikatów; przypisany klaster.

**3.3 Horyzonty nowych pytań w wydaniu.** Ok. 40% z terminem do daty następnego wydania (14 dni); ok. 40% do końca kwartału (31.12.2026); ok. 20% dłuższe.

**3.4 Klaster.** Etykieta grupy pytań zależnych od tego samego rozstrzygnięcia, np. ORMUZ, BAB_EL_MANDAB, UA_ROZMOWY, UA_FRONT, FLANKA, USA_EUROPA, CN_ZIEMIE_RZADKIE, TAJWAN, ENERGIA_UE, ROPA_CENA, STOPY, USA_WYBORY, RU_FINANSE, SAHEL, WENEZUELA.

**3.5 p_status_quo.** Prawdopodobieństwo mechaniczne „co się stanie, jeśli nikt nie podejmie nowej decyzji”:
- 0.10 — gdy TAK wymaga zmiany obecnego stanu,
- 0.90 — gdy TAK oznacza trwanie obecnego stanu,
- 0.50 — gdy status quo nie da się określić.

Ustalane przy tworzeniu pytania, bez patrzenia na jakiekolwiek prognozy.

**3.6 czyj_sukces.** Wpisz aktora tylko wtedy, gdy TAK wyraźnie wzmacnia jego pozycję kosztem innego. W pozostałych przypadkach BRAK. Wątpliwość rozstrzygaj na korzyść BRAK.

**3.7 Anulowanie.** Kryterium okazało się niejednoznaczne albo źródło rozstrzygnięcia przestało istnieć → status ANULOWANE z uzasadnieniem. Pytanie nie wchodzi do wyników.

**3.8 Trywialność.** Najwyżej 20% aktywnych pytań może mieć AGR_RT poniżej 0.05 lub powyżej 0.95. Przy przekroczeniu — w kolejnym wydaniu dodaj trudniejsze pytania.

## 4. Soczewki (trzy niezależne, ślepe przebiegi)

**A — „Rozgrywka mocarstw”.** Kto decyduje; interesy i wypłaty każdej strony; zdolności i ograniczenia; dostępne alternatywy; który ruch jest dla kogo opłacalny; jaka równowaga ruchów wynika do terminu; co musiałoby się stać, żeby równowaga się przesunęła.

**B — „Widok z zewnątrz”.** Klasa odniesienia i częstość bazowa; trwałość status quo; czas pozostały do terminu (przy stałym tempie zdarzeń: p ≈ 1 − (1 − r)^t); korekta o specyfikę przypadku dopiero na końcu i ostrożnie. Narracja zredukowana do minimum.

**C — „Ograniczenia wewnętrzne i ekonomiczne”.** Polityka wewnętrzna i kalendarze wyborcze; bodźce osobiste przywódców (legitymizacja, relacje personalne); budżety, rynki, logistyka; procedury i terminy instytucjonalne (np. kalendarz budżetowy, kroki prawne, notyfikacje w Kongresie).

Każda soczewka dla każdego aktywnego pytania podaje: p, uzasadnienie w 1–2 zdaniach w swojej logice, kluczowy wskaźnik, pewność analityczną oraz zmianę względem własnej poprzedniej prognozy z powodem.

## 5. Agregacja i red team

- **AGR** = średnia arytmetyczna A, B, C.
- **Red team** (etap 05) proponuje korekty wyłącznie na podstawie konkretnego dowodu albo błędu logicznego (w tym niespójności między pytaniami). Limit: ±0.15 na pytanie. Bez korekt „dla bezpieczeństwa”.
- **AGR_RT** = AGR + zaakceptowane korekty (w etapie 06). Bez korekty AGR_RT = AGR.
- **Prognozą oficjalną jest AGR_RT.** Rejestr zawiera wszystkie przebiegi, co pozwala zmierzyć, czy red team pomaga.

## 6. Benchmarki zewnętrzne

- Wyłącznie w etapie 06, **po** commicie „prognozy zamrożone”.
- Źródła: Metaculus, Good Judgment Open, Polymarket, Kalshi, Manifold, RAND Forecasting Initiative.
- Dopasowanie: DOKLADNE (to samo zdarzenie, termin ±7 dni, zbliżone kryterium) albo PRZYBLIZONE. Do wyników wchodzą tylko DOKLADNE.
- Prognozy tego wydania nie zmieniają się po zobaczeniu benchmarków. W kolejnych wydaniach soczewki nadal ich nie widzą.
- Benchmarki trafiają tylko do `07_zalacznik_benchmarki.md`, nie do raportu głównego.

## 7. Rozstrzyganie

- Każde rozstrzygnięcie ma dowód (URL, wydawca, data). Dla pytań z PIR — dwa niezależne źródła.
- Pytanie „czy do daty X zdarzy się Y” rozstrzyga się na TAK w dniu zajścia Y, na NIE po upływie X.
- Flaga WERYFIKUJ: pytania niejednoznaczne, sporne oraz losowe 20% pozostałych (ziarno losowania = numer wydania). Flagi zatwierdza użytkownik.

## 8. Wyniki

- **Brier** = (p − o)², gdzie o ∈ {0, 1}. Liczony dla każdej prognozy w każdym wydaniu osobno oraz jako średnia na pytanie.
- **BSS** = 1 − Brier_model / Brier_odniesienia.
- **Kalibracja:** przedziały co 10 punktów procentowych.
- **Błąd kierunkowy:** średnia (p − o) w grupach `czyj_sukces` (bez BRAK). Neutralne źródło lub metoda ma średnią bliską 0 w każdej grupie.
- **Klastry:** wyniki także z wagą 1 na klaster.
- **Przebiegi:** Brier A vs B vs C vs AGR vs AGR_RT.
- **Uwaga statystyczna:** poniżej ~30 rozstrzygniętych pytań wyniki są orientacyjne; różnic przebiegów nie interpretuje się przed przeglądem kwartalnym.

## 9. Źródła i fakty

- Rekord faktu (tabela w `02_fakty/G*.md`): ID | data | aktor | działanie | adresat | wektor | region | status | wydawca | URL | ocena źródła | perspektywa | PIR.
- Zdarzenia kluczowe: trzy perspektywy (Z, A, T); wyszukiwanie w języku aktora (RU, ZH, AR, FA, TR; dla Indii — media anglojęzyczne).
- Źródła państwowe: dopuszczalne jako fakt o wypowiedzi i jako perspektywa; nigdy jako jedyne potwierdzenie zdarzenia spornego.
- Wikipedia: wyłącznie indeks chronologii.
- Mapa źródeł: `zrodla/mapa_zrodel.md`.

## 10. Skala słowna prawdopodobieństwa (tekst raportu)

Prawie wykluczone 1–5% · bardzo mało prawdopodobne 5–20% · mało prawdopodobne 20–45% · mniej więcej równe szanse 45–55% · prawdopodobne 55–80% · bardzo prawdopodobne 80–95% · prawie pewne 95–99%.

## 11. Struktura raportu wydania

Nagłówek (numer, data stanu, konwencja oznaczeń) → Streszczenie wykonawcze (6–8 akapitów) → **0. Wyniki trafności** (od wydania 02) → A. Cele strategiczne mocarstw → B. Punkty tarcia → C. Przesmyki i lokalizacje → D. Surowce i łańcuchy dostaw → E. Przesunięcia orientacji państw → F. Rywalizacja gospodarcza i technologiczna → G. Mapa zmian wpływów → H. Scenariusze i prognozy (scenariusze 6–12 mies. / 2–3 lata / 5–10 lat z prawdopodobieństwami; pełna lista prognoz AGR_RT wg wektorów, z rozrzutem soczewek i zmianą vs poprzednie wydanie) → I. Tabela najistotniejszych zmian → J. Niepewności i braki → K. Wnioski dla Polski (K.1–K.7) → L. Blok stanu.

Sekcje B–F kończą się akapitem „Mechanizm” i linią „Dla Polski”. Tytuły sekcji bez zmian między wydaniami.

## 12. Czego nie zmieniamy do przeglądu kwartalnego

Soczewki, reguły agregacji i red teamu, panel stały, skale, definicje wyników. Poprawki procesu — tylko po akceptacji użytkownika i wpisie do `zmiany_metodologii.md`.
