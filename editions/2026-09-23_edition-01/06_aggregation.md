# Etap 06 — Agregacja (wydanie 01, stan 23.09.2026)

Wejście: `rejestr/pytania.csv` (73 pytania AKTYWNE), `rejestr/prognozy.csv` (przebiegi A, B, C z wydania 01), `05_red_team.md` §3.
Kontrola kompletności: wszystkie 73 aktywne pytania mają prognozę każdej z trzech soczewek — agregacja dopuszczalna.

Konwencja zapisu: AGR = średnia arytmetyczna A, B, C, zapisana z dokładnością do 0.001 (bez dodatkowego zaokrąglania). AGR_RT = AGR + przyjęta korekta (dokładnie, 0.001), przycięte do 0.01–0.99; bez korekty AGR_RT = AGR. Wartości w tabeli 05 §3 (np. 0.94 dla Q-0013) są zaokrągleniami prezentacyjnymi tych samych liczb. Pewność analityczna AGR i AGR_RT = mediana pewności trzech soczewek.

## 1. Korekty red teamu — decyzje

Kryteria przyjęcia (metodologia §5, prompt 06 krok 1.2): |korekta| ≤ 0.15 oraz konkretny dowód albo wskazany błąd logiczny.

| ID | AGR | korekta | AGR_RT | typ (05) | decyzja | podstawa |
|---|---|---|---|---|---|---|
| Q-0054 | 0.820 | +0.12 | 0.940 | dowód | PRZYJĘTA | wynik SR rósł z liczeniem (4,96% → 5,00%); doniesienie Meduzy 22.09 o dopisaniu głosów; B nie znała C-01 |
| Q-0013 | 0.843 | +0.10 | 0.943 | logika + dowód | PRZYJĘTA | baza CPI IX 2025 = 0,0% m/m (GUS); rachunek soczewek daje ok. 4,2–4,4% r/r |
| Q-0040 | 0.567 | +0.10 | 0.667 | dowód | PRZYJĘTA | udokumentowana klasa odniesienia (3 z 3 zim z incydentem i śledztwem); A bez argumentu za NIE |
| Q-0062 | 0.433 | +0.08 | 0.513 | logika | PRZYJĘTA | luka w zbieraniu (03 §1.7 p. 10) potraktowana w soczewkach jak brak zdarzeń; tempo VII–VIII |
| Q-0003 | 0.333 | +0.07 | 0.403 | dowód + spójność | PRZYJĘTA | G1-031: §1249 to procedura certyfikacji; niespójność z ACH-3 (03) |
| Q-0050 | 0.333 | +0.05 | 0.383 | dowód | PRZYJĘTA | notowanie 23.09: 8,99 zł/l (C-04) wobec wyjściowych 8,89 zł/l w A i B |
| Q-0002 | 0.050 | +0.01 | 0.060 | logika | PRZYJĘTA | podwójne liczenie tego samego dowodu w soczewce B |
| Q-0031 | 0.157 | −0.05 | 0.107 | logika | PRZYJĘTA | uzasadnienie C wskazuje niższe p niż podane |
| Q-0039 | 0.217 | −0.07 | 0.147 | dowód | PRZYJĘTA | dane ACP (zaostrzenie od 01.10), opady −34%, El Niño; A bez danych |

**Odrzucone korekty: brak.** Żadna z 9 propozycji nie przekracza ±0.15 i każda ma wskazany dowód albo błąd logiczny. Pytania, które red team rozważył i sam odrzucił (Q-0004, Q-0016, Q-0067, Q-0070, Q-0055, Q-0060, Q-0008), mają AGR_RT = AGR.

Uwaga do zapisu: przyjęcie korekty nie oznacza weryfikacji dowodu w etapie 06 — etap sprawdza wymogi formalne (limit, obecność dowodu lub błędu). Korekta Q-0054 opiera się częściowo na wartości 5,13% (C-01), której red team nie potwierdził; kierunek korekty podtrzymują potwierdzone 5,00% przy 96,95% protokołów.

## 2. Tabela AGR i AGR_RT (73 pytania)

| ID | wektor | klaster | A | B | C | rozrzut | AGR | korekta RT | AGR_RT | pewność |
|---|---|---|---|---|---|---|---|---|---|---|
| Q-0001 | MIL | RU_MOBILIZACJA | 0.03 | 0.03 | 0.03 | 0.00 | 0.030 | — | **0.030** | średnia |
| Q-0002 | MIL | FLANKA | 0.05 | 0.05 | 0.05 | 0.00 | 0.050 | +0.01 | **0.060** | średnia |
| Q-0003 | MIL | USA_EUROPA | 0.35 | 0.35 | 0.30 | 0.05 | 0.333 | +0.07 | **0.403** | niska |
| Q-0004 | MIL | UA_FRONT | 0.18 | 0.15 | 0.35 | 0.20 | 0.227 | — | **0.227** | średnia |
| Q-0005 | MIL | TAJWAN | 0.25 | 0.35 | 0.40 | 0.15 | 0.333 | — | **0.333** | niska |
| Q-0006 | ENE | ROPA_CENA | 0.35 | 0.45 | 0.40 | 0.10 | 0.400 | — | **0.400** | średnia |
| Q-0007 | ENE | ROPA_CENA | 0.12 | 0.25 | 0.20 | 0.13 | 0.190 | — | **0.190** | niska |
| Q-0008 | ENE | ROPA_CENA | 0.15 | 0.30 | 0.15 | 0.15 | 0.200 | — | **0.200** | niska |
| Q-0009 | ENE | ENERGIA_UE | 0.25 | 0.35 | 0.30 | 0.10 | 0.300 | — | **0.300** | niska |
| Q-0010 | ENE | ENERGIA_UE | 0.40 | 0.25 | 0.40 | 0.15 | 0.350 | — | **0.350** | niska |
| Q-0011 | GOS | USA_CHINY_HANDEL | 0.72 | 0.75 | 0.78 | 0.06 | 0.750 | — | **0.750** | średnia |
| Q-0012 | GOS | RU_SANKCJE_USA | 0.20 | 0.15 | 0.22 | 0.07 | 0.190 | — | **0.190** | niska |
| Q-0013 | GOS | PL_INFLACJA | 0.80 | 0.85 | 0.88 | 0.08 | 0.843 | +0.10 | **0.943** | średnia |
| Q-0014 | GOS | ZYWNOSC | 0.55 | 0.55 | 0.58 | 0.03 | 0.560 | — | **0.560** | niska |
| Q-0015 | GOS | USA_UE_HANDEL | 0.12 | 0.12 | 0.08 | 0.04 | 0.107 | — | **0.107** | średnia |
| Q-0016 | FIN | STOPY_PL | 0.15 | 0.10 | 0.30 | 0.20 | 0.183 | — | **0.183** | średnia |
| Q-0017 | FIN | STOPY_EBC | 0.45 | 0.45 | 0.40 | 0.05 | 0.433 | — | **0.433** | niska |
| Q-0018 | FIN | CN_SANKCJE_WTORNE | 0.10 | 0.08 | 0.08 | 0.02 | 0.087 | — | **0.087** | średnia |
| Q-0019 | FIN | RU_SANKCJE_UE | 0.55 | 0.50 | 0.40 | 0.15 | 0.483 | — | **0.483** | niska |
| Q-0020 | FIN | STOPY_RU | 0.30 | 0.25 | 0.20 | 0.10 | 0.250 | — | **0.250** | średnia |
| Q-0021 | TEC | CN_ZIEMIE_RZADKIE | 0.63 | 0.70 | 0.72 | 0.09 | 0.683 | — | **0.683** | średnia |
| Q-0022 | TEC | CN_ZIEMIE_RZADKIE | 0.60 | 0.72 | 0.72 | 0.12 | 0.680 | — | **0.680** | średnia |
| Q-0023 | TEC | USA_CHINY_TECH | 0.35 | 0.50 | 0.45 | 0.15 | 0.433 | — | **0.433** | niska |
| Q-0024 | TEC | USA_CHINY_TECH | 0.15 | 0.15 | 0.20 | 0.05 | 0.167 | — | **0.167** | niska |
| Q-0025 | TEC | CN_ZIEMIE_RZADKIE | 0.45 | 0.60 | 0.45 | 0.15 | 0.500 | — | **0.500** | niska |
| Q-0026 | DYP | UA_ROZMOWY | 0.45 | 0.45 | 0.45 | 0.00 | 0.450 | — | **0.450** | niska |
| Q-0027 | DYP | FLANKA | 0.10 | 0.12 | 0.12 | 0.02 | 0.113 | — | **0.113** | średnia |
| Q-0028 | DYP | ORMUZ | 0.35 | 0.25 | 0.30 | 0.10 | 0.300 | — | **0.300** | niska |
| Q-0029 | DYP | USA_CHINY_SZCZYTY | 0.50 | 0.60 | 0.50 | 0.10 | 0.533 | — | **0.533** | niska |
| Q-0030 | DYP | UA_ROZMOWY | 0.30 | 0.25 | 0.25 | 0.05 | 0.267 | — | **0.267** | niska |
| Q-0031 | WEW | USA_WYBORY | 0.15 | 0.12 | 0.20 | 0.08 | 0.157 | -0.05 | **0.107** | średnia |
| Q-0032 | WEW | IRAN_WLADZA | 0.15 | 0.12 | 0.15 | 0.03 | 0.140 | — | **0.140** | niska |
| Q-0033 | WEW | BRAZYLIA_WYBORY | 0.55 | 0.57 | 0.55 | 0.02 | 0.557 | — | **0.557** | niska |
| Q-0034 | WEW | WENEZUELA | 0.30 | 0.35 | 0.35 | 0.05 | 0.333 | — | **0.333** | niska |
| Q-0035 | WEW | SAHEL | 0.08 | 0.10 | 0.10 | 0.02 | 0.093 | — | **0.093** | niska |
| Q-0036 | INF | ORMUZ | 0.30 | 0.20 | 0.22 | 0.10 | 0.240 | — | **0.240** | niska |
| Q-0037 | INF | ORMUZ | 0.10 | 0.12 | 0.12 | 0.02 | 0.113 | — | **0.113** | niska |
| Q-0038 | INF | ORMUZ | 0.32 | 0.22 | 0.30 | 0.10 | 0.280 | — | **0.280** | niska |
| Q-0039 | INF | PANAMA | 0.35 | 0.10 | 0.20 | 0.25 | 0.217 | -0.07 | **0.147** | niska |
| Q-0040 | INF | BALTYK_INFRA | 0.40 | 0.75 | 0.55 | 0.35 | 0.567 | +0.10 | **0.667** | niska |
| Q-0041 | MIL | IRAN_WOJNA | 0.05 | 0.08 | 0.05 | 0.03 | 0.060 | — | **0.060** | średnia |
| Q-0042 | DYP | ORMUZ | 0.55 | 0.45 | 0.45 | 0.10 | 0.483 | — | **0.483** | niska |
| Q-0043 | MIL | BAB_EL_MANDAB | 0.40 | 0.35 | 0.35 | 0.05 | 0.367 | — | **0.367** | niska |
| Q-0044 | MIL | USA_EUROPA | 0.20 | 0.20 | 0.20 | 0.00 | 0.200 | — | **0.200** | niska |
| Q-0045 | MIL | FLANKA | 0.25 | 0.15 | 0.15 | 0.10 | 0.183 | — | **0.183** | niska |
| Q-0046 | MIL | KOREA | 0.50 | 0.45 | 0.40 | 0.10 | 0.450 | — | **0.450** | niska |
| Q-0047 | MIL | TAJWAN | 0.40 | 0.40 | 0.55 | 0.15 | 0.450 | — | **0.450** | niska |
| Q-0048 | ENE | ENERGIA_UE | 0.35 | 0.37 | 0.40 | 0.05 | 0.373 | — | **0.373** | niska |
| Q-0049 | ENE | ENERGIA_UE | 0.70 | 0.60 | 0.55 | 0.15 | 0.617 | — | **0.617** | niska |
| Q-0050 | ENE | PALIWA_PL | 0.30 | 0.35 | 0.35 | 0.05 | 0.333 | +0.05 | **0.383** | niska |
| Q-0051 | ENE | OPEC | 0.30 | 0.30 | 0.25 | 0.05 | 0.283 | — | **0.283** | niska |
| Q-0052 | FIN | PLN | 0.45 | 0.47 | 0.45 | 0.02 | 0.457 | — | **0.457** | niska |
| Q-0053 | FIN | RU_FINANSE | 0.50 | 0.45 | 0.52 | 0.07 | 0.490 | — | **0.490** | niska |
| Q-0054 | WEW | RU_WEW | 0.85 | 0.68 | 0.93 | 0.25 | 0.820 | +0.12 | **0.940** | średnia |
| Q-0055 | WEW | LOTWA_WYBORY | 0.75 | 0.88 | 0.82 | 0.13 | 0.817 | — | **0.817** | średnia |
| Q-0056 | WEW | BRAZYLIA_WYBORY | 0.08 | 0.04 | 0.07 | 0.04 | 0.063 | — | **0.063** | średnia |
| Q-0057 | GOS | USA_CHINY_HANDEL | 0.12 | 0.12 | 0.15 | 0.03 | 0.130 | — | **0.130** | średnia |
| Q-0058 | GOS | USA_CHINY_HANDEL | 0.45 | 0.45 | 0.45 | 0.00 | 0.450 | — | **0.450** | niska |
| Q-0059 | DYP | UA_ROZMOWY | 0.15 | 0.10 | 0.10 | 0.05 | 0.117 | — | **0.117** | średnia |
| Q-0060 | FIN | CN_SANKCJE_WTORNE | 0.55 | 0.68 | 0.45 | 0.23 | 0.560 | — | **0.560** | niska |
| Q-0061 | FIN | RU_SANKCJE_USA | 0.25 | 0.15 | 0.25 | 0.10 | 0.217 | — | **0.217** | niska |
| Q-0062 | INF | BAB_EL_MANDAB | 0.45 | 0.45 | 0.40 | 0.05 | 0.433 | +0.08 | **0.513** | niska |
| Q-0063 | INF | ORMUZ | 0.45 | 0.40 | 0.40 | 0.05 | 0.417 | — | **0.417** | niska |
| Q-0064 | DYP | UA_USA | 0.25 | 0.25 | 0.30 | 0.05 | 0.267 | — | **0.267** | niska |
| Q-0065 | MIL | IRAN_WOJNA | 0.25 | 0.28 | 0.25 | 0.03 | 0.260 | — | **0.260** | niska |
| Q-0066 | FIN | STOPY_FED | 0.30 | 0.40 | 0.30 | 0.10 | 0.333 | — | **0.333** | niska |
| Q-0067 | ENE | ENERGIA_UE | 0.30 | 0.45 | 0.30 | 0.15 | 0.350 | — | **0.350** | średnia |
| Q-0068 | MIL | BAB_EL_MANDAB | 0.25 | 0.25 | 0.20 | 0.05 | 0.233 | — | **0.233** | niska |
| Q-0069 | MIL | TAJWAN | 0.15 | 0.15 | 0.20 | 0.05 | 0.167 | — | **0.167** | niska |
| Q-0070 | FIN | PL_FINANSE | 0.30 | 0.33 | 0.30 | 0.03 | 0.310 | — | **0.310** | niska |
| Q-0071 | FIN | UA_FINANSOWANIE | 0.20 | 0.12 | 0.20 | 0.08 | 0.173 | — | **0.173** | niska |
| Q-0072 | DYP | KAUKAZ | 0.12 | 0.15 | 0.12 | 0.03 | 0.130 | — | **0.130** | średnia |
| Q-0073 | MIL | UA_FRONT | 0.10 | 0.10 | 0.15 | 0.05 | 0.117 | — | **0.117** | średnia |

Średnia AGR: 0.332 · średnia AGR_RT: 0.338 · min AGR_RT 0.030 · max AGR_RT 0.943

## 3. Test trywialności (§3.8)

- AGR_RT < 0.05 lub > 0.95: **1 z 73 pytań (1,4%)** — Q-0001 (0.030). Limit: 20% (14 pytań).
- Najbliżej progu górnego: Q-0013 (0.943), Q-0054 (0.940) — poniżej 0.95.
- **Wynik: reguła spełniona.** Nie ma obowiązku dodawania trudniejszych pytań w wydaniu 02.

## 4. Rejestr

Do `rejestr/prognozy.csv` dopisano 146 wierszy (73 × AGR, 73 × AGR_RT), data 2026-09-23, wydanie 01. Istniejące wiersze bez zmian (sprawdzone porównaniem bajtowym). Liczba zaakceptowanych korekt: 9; pytania z AGR_RT ≠ AGR: 9.
