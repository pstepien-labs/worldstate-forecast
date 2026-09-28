# Załącznik: porównanie z tłumem i rynkami — wydanie 01 (stan 23.09.2026)

> **Plik zakazany dla etapów 03, 04 i 05 we wszystkich przyszłych wydaniach** (CLAUDE.md p. 8). Nie jest częścią raportu głównego (metodologia §6). Materiał do przeglądu metody, nie podstawa do zmiany prognoz.

Źródło: `06_benchmarki.md` i `rejestr/benchmarki.csv` (43 wiersze, 26 pytań). Notowania zebrano 23.09.2026 wieczorem (czas PL), **po** commicie „wydanie-01 prognozy zamrożone” (32a635e). Żadnej prognozy nie zmieniono. Δ = tłum − AGR_RT.

## 1. Dostęp do źródeł

| Źródło | Dostęp | Wiersze |
|---|---|---|
| Polymarket | publiczne API tylko do odczytu (strona: ECONNREFUSED dla narzędzia) | 25 |
| Kalshi | publiczne API tylko do odczytu | 13 |
| Manifold | publiczne API (waluta gry, zwykle niska płynność) | 9 |
| Good Judgment Open | strony publiczne, bez logowania | 2 |
| Metaculus | API wymaga konta, strony HTTP 403; nie logowano się | 0 |
| RAND Forecasting Initiative | platforma zamknięta (tylko archiwum) | 0 |

Z sześciu źródeł z metodologii §6 działają cztery — uwaga do przeglądu kwartalnego.

## 2. Pytania z dopasowaniem DOKLADNE (wchodzą do BSS vs tłum)

Gdy pytanie ma kilka źródeł, `wyniki.py` uśrednia je — tak też liczy kolumna „tłum (średnia)”.

| ID | Pytanie (skrót) | Termin | AGR_RT | Źródła (p) | Tłum (średnia) | Δ |
|---|---|---|---|---|---|---|
| Q-0001 | Dekret o mobilizacji RU | 31.12.2026 | 0.03 | Manifold 0.27 | 0.270 | **+0.24** |
| Q-0006 | Brent > 100 USD w dniu 06.10 | 06.10.2026 | 0.40 | Kalshi 0.42 (termin 30.09) | 0.420 | +0.02 |
| Q-0020 | Bank Rosji obniża stopę 23.10 | 23.10.2026 | 0.25 | Polymarket 0.275 | 0.275 | +0.03 |
| Q-0027 | Wniosek z art. 4 NATO | 31.12.2026 | 0.113 | Polymarket 0.47 | 0.470 | **+0.36** |
| Q-0031 | Republikanie ≥ 218 mandatów | 31.12.2026 | 0.107 | Polymarket 0.075; Kalshi 0.082; Manifold 0.062 | 0.073 | −0.03 |
| Q-0033 | Lula wygrywa wybory | 31.10.2026 | 0.557 | Polymarket 0.405; Kalshi 0.435; Manifold 0.373; GJO 0.50 | 0.428 | −0.13 |
| Q-0036 | Ormuz: średnia 7-dniowa > 40 | 31.12.2026 | 0.24 | Kalshi 0.18 | 0.180 | −0.06 |
| Q-0037 | Ormuz: ≥ 20 przejść w dobie | 07.10.2026 | 0.113 | Polymarket 0.041 (termin 30.09) | 0.041 | −0.07 |
| Q-0054 | Sprawiedliwa Rosja ≥ 5,00% | 30.09.2026 | 0.94 | Polymarket 0.99 | 0.990 | +0.05 |
| Q-0055 | Zjednoczona Lista wygrywa na Łotwie | 10.10.2026 | 0.817 | Polymarket 0.95; Kalshi 0.925 | 0.938 | +0.12 |
| Q-0056 | Lula > 50% w I turze | 05.10.2026 | 0.063 | Manifold 0.099 | 0.099 | +0.04 |
| Q-0066 | FOMC podnosi stopę 28.10 | 28.10.2026 | 0.333 | Polymarket 0.65; Kalshi 0.67; Manifold 0.618 | 0.646 | **+0.31** |

Średnia |Δ| na 12 pytaniach: 0.12. Rozbieżności ≥ 0.20: 3 (Q-0027, Q-0066, Q-0001). Tłum jest wyżej niż AGR_RT w 8 z 12 pytań, niżej w 4. Wszystkie trzy różnice ≥ 0.20 mają ten sam znak: tłum daje wyższe p zdarzeniom rzadkim albo decyzjom instytucji (mobilizacja, art. 4, podwyżka Fed). Przy n = 12 to obserwacja orientacyjna, nie wniosek o metodzie.

## 3. Wszystkie dopasowania (DOKLADNE i PRZYBLIZONE)

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

Brak odpowiedników dla 47 pytań, m.in. całego panelu ENE poza Brentem 06.10 (TTF, magazyny AGSI+, olej napędowy), CPI w Polsce, EUR/PLN, budżetu Rosji, ceł z H.R. 5334, magnesów, Blackwell, kabli bałtyckich, Kanału Panamskiego, KRLD, Tajwanu, 22. pakietu UE, aktywów Banku Rosji, Armenii i Azerbejdżanu.

## 4. Rozbieżności |Δ| ≥ 0.20 — hipotezy przyczyn

Hipotezy robocze z etapu 06; nie rozstrzygają, kto ma rację. Rozstrzygnie wynik.

**DOKLADNE**
1. **Q-0066 FOMC 28.10** (0.333 vs 0.62–0.67; trzy rynki zgodne, Kalshi ok. 770 tys. kontraktów). Soczewki A i C zakładały odłożenie podwyżki na XII z powodu wyborów 03.11. Hipoteza: brak wyceny kontraktów fed funds w materiale soczewek i przecenienie argumentu wyborczego — to ten sam mechanizm „hamulca wyborczego” (Z1), który red team wskazał jako ryzyko skorelowanego błędu.
2. **Q-0027 art. 4 NATO** (0.113 vs 0.47; niska płynność, widełki 0.41/0.53). Częstość bazowa z lat 2022–2025 (ok. 0,65/rok) daje dla 3,3 mies. ok. 0,16, nie 0,47. Hipoteza: płytki rynek albo informacja o incydentach, której soczewki nie miały. Sprawdzić w etapie 01 wydania 02.
3. **Q-0001 mobilizacja RU** (0.03 vs 0.27 Manifold, 17 graczy; Polymarket 0.26 przy szerszym kryterium). Hipoteza: (a) rynek Polymarket liczy rozszerzenie kategorii w dekrecie z IX 2022 — zdarzenie tańsze dla Kremla niż nowy dekret; (b) premia za ogon na rynkach wojennych.

**PRZYBLIZONE (poza wynikami)**
4. **Q-0030 Putin–Trump** (0.267 vs 0.765 do 31.12). Rynek zakłada spotkanie przy APEC w Shenzhen (18–19.11), gdzie wystarczy uścisk dłoni; soczewki traktowały spotkanie jako osobny szczyt i nie rozważyły wspólnej obecności na APEC. **Najpoważniejsza rozbieżność wydania — pominięty scenariusz, nie różnica ocen.** Do przeglądu spójność z Q-0029 (Trump na APEC, 0.533).
5. **Q-0026 spotkanie trójstronne** (0.45 vs 0.035 Kalshi — szczebel przywódców; 0.645 Polymarket — kontakt RU–UA). Rozbieżność kryterialna.
6. **Q-0058 i Q-0011 rozejm USA–ChRL** — rynki różnią się między sobą o 0.40; płytkie i odległe kryterialnie.
7. **Q-0065 uderzenie USA na Iran do 31.12** (0.26 vs 0.545 „zerwania rozejmu”) — rynek jest górną granicą dla naszego pytania, ale rozbieżność jest duża; zbieżna z ryzykami Z1 i pominięcia Izraela.
8. **Q-0017 EBC** (0.433 vs 0.64 na XII, płynność ok. 4 tys. USD; rynek X: 0.48) — soczewki przeważyły konsensus ekonomistów nad wyceną kontraktów.
9. **Q-0018 bank z ChRL na SDN** (0.087 vs 0.315) — kryterium rynku szersze; rozbieżność nieinformatywna.

**Poniżej progu, warte odnotowania:** Q-0033 Lula (rynki 0.37–0.44 przy wysokiej płynności vs 0.557); Q-0055 Łotwa (0.93–0.95 vs 0.817).

## 5. Wnioski do przeglądu kwartalnego (bez zmiany prognoz)

- Jedna z trzech rozbieżności DOKLADNE (Q-0066) i dwie PRZYBLIZONE (Q-0065, pośrednio Q-0030) dotyczą tego samego obszaru ryzyka: skorelowanego założenia o hamulcu wyborczym i o kalendarzu szczytów. Wynik tych pytań trzeba czytać jako jeden zakład.
- Soczewki nie korzystały z wycen instrumentów finansowych (kontrakty na stopy), choć nie są one rynkami predykcyjnymi w rozumieniu CLAUDE.md p. 9. Czy dopuścić je jako dane wejściowe soczewki B — decyzja przeglądu kwartalnego, nie tego wydania.
- Niespójność międzyrynkowa (Ormuz: Polymarket P(≥ 60) = 0.205 > Kalshi P(> 40) = 0.18) pokazuje, że pojedyncze notowania na płytkich rynkach mają szum rzędu 0.05–0.10.
