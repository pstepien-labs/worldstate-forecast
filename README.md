# Skalibrowana prognoza układu sił — pakiet startowy

**Misja:** przewidywać ruchy mocarstw trafniej niż proste punkty odniesienia — i udowadniać to pomiarem.

Pakiet to zestaw plików dla Claude Code (model Claude Opus 5, z dostępem do sieci). To nie jest oprogramowanie: jedyny skrypt (`narzedzia/wyniki.py`) liczy wyniki trafności. Wszystko inne to instrukcje w Markdown i rejestr w CSV.

## Wymagania

- Claude Code z modelem Claude Opus 5 i dostępem do wyszukiwania i pobierania stron.
- `git` i `python3` (bez dodatkowych bibliotek).
- Opcjonalnie `pandoc` — do generowania PDF raportu.

## Zawartość

| Ścieżka | Co to jest |
|---|---|
| `CLAUDE.md` | Reguły stałe; Claude Code wczytuje je automatycznie w każdej sesji w tym katalogu |
| `metodologia/metodologia_v1.0.md` | Metoda zamrożona do przeglądu kwartalnego |
| `prompty/00–08, M, Q` | Instrukcje etapów, mini-retrospektywy i przeglądu kwartalnego |
| `.claude/commands/` | Skróty `/g00` … `/g08`, `/gM`, `/gQ` uruchamiające etapy |
| `rejestr/*.csv` | Pytania, prognozy, benchmarki, rozstrzygnięcia, źródła (tylko do dopisywania) |
| `rejestr/pytania_propozycje_z_wydania_00.csv` | 28 propozycji pytań do panelu, do weryfikacji w wydaniu 01 |
| `zrodla/mapa_zrodel.md` | Źródła według aktorów i perspektyw |
| `wydania/2026-09-21_wydanie-00/` | Punkt wyjścia: raport PDF i blok stanu |
| `narzedzia/wyniki.py` | Liczenie Briera, BSS, kalibracji, błędu kierunkowego, bootstrapu |

## Jak uruchomić jedno wydanie

W terminalu, w katalogu pakietu: `claude`, potem `/model`, wybierz Opus 5. Każdy etap uruchamiaj w **nowej sesji** (`/clear` między etapami). Etapy przekazują sobie wyniki przez pliki.

| Krok | Komenda | Czas orientacyjny | Uwagi |
|---|---|---|---|
| 1 | `/g00 2026-10-05 01` | 15–30 min | data stanu i numer wydania |
| 2 | `/g01` | 0–60 min | w wydaniu 01 zwykle pusty |
| — | **Ty** | 10–20 min | przejrzyj sekcję „DO WERYFIKACJI” w `01_rozstrzygniecia.md` |
| 3–6 | `/g02 G1`, `/g02 G2`, `/g02 G3`, `/g02 G4` | 1–3 h każda | najcięższy etap; przerwaną grupę uruchom ponownie tą samą komendą |
| 7 | `/g03` | 1–2 h | analiza i bank pytań |
| 8–10 | `/g04 A`, `/g04 B`, `/g04 C` | ~1 h każda | trzy osobne sesje, koniecznie po `/clear` |
| 11 | `/g05` | ~1 h | red team |
| 12 | `/g06` | ~1 h | zamrożenie prognoz, potem benchmarki |
| 13 | `/g07` | 1–2 h | raport |
| 14 | `/g08` | 30–60 min | kontrola jakości, tag git |

Łącznie ok. 12–20 godzin pracy agenta na wydanie. Rozłóż etapy na 2–3 dni. Jeśli skróty nie działają w Twojej wersji Claude Code, wpisz ręcznie: „Przeczytaj CLAUDE.md, wydania/AKTUALNE.md i prompty/0X_….md, wykonaj etap. Parametry: …”.

Uprawnienia: Claude Code będzie prosić o zgodę na wyszukiwanie, pobieranie stron, `git` i `python3`. Możesz je zezwolić na stałe dla tego projektu przez `/permissions`. Nie wyłączaj pytań o uprawnienia globalnie.

## Plan pierwszych trzech iteracji

**Wydanie 01 — stan 05.10.2026: „Rozruch z pomiarem”.**
- Pełne zbieranie w czterech grupach wektorów.
- Ustalenie panelu 40 pytań z propozycji z wydania 00 plus 20–40 pytań swobodnych.
- Ok. 40% pytań z terminem do 19.10, żeby wydanie 02 miało pierwsze rozstrzygnięcia.
- Pierwsze ślepe prognozy trzech soczewek, red team, zamrożenie, benchmarki, raport.

**Wydanie 02 — stan 19.10.2026: „Pierwsza pętla zwrotna”.**
- Pierwsze rozstrzygnięcia i wyniki orientacyjne.
- Zbieranie w trybie „zmiany i weryfikacja”: fakty z 01 potwierdzone albo usunięte z uzasadnieniem.
- Większy udział źródeł strony-aktora przy zdarzeniach kluczowych.

**Wydanie 03 — stan 02.11.2026: „Przed skupiskiem dat”.**
- Tuż przed 03.11 (wybory w USA), 10.11 (ziemie rzadkie) i 18–19.11 (APEC). Wiele pytań rozstrzygnie się w ciągu trzech tygodni — dobry test.
- Po wydaniu: `/gM` — mini-retrospektywa **procesu** (bez zmian metody).

Dalej: wydania 04–06 (16.11, 30.11, 14.12) bez zmian metody i przegląd kwartalny `/gQ` ok. 21.12.2026.

## Co robisz Ty

1. Zatwierdzasz rozstrzygnięcia z flagą WERYFIKUJ (nowy wiersz z wyższą `wersja` w `rejestr/rozstrzygniecia.csv`).
2. Akceptujesz albo odrzucasz propozycje z mini-retrospektywy i przeglądu kwartalnego.
3. Raz na wydanie czytasz `08_kontrola.md`: czy nie było naruszeń ślepoty prognoz i edycji historii rejestru.

## Trzy reguły, których nie wolno łamać

1. **Rejestr tylko do dopisywania.** Historia prognoz jest dowodem; git to potwierdza.
2. **Ślepota prognoz.** Soczewki i red team nie widzą benchmarków ani siebie nawzajem.
3. **Metoda zamrożona na kwartał.** Inaczej nie da się stwierdzić, co pomogło.
