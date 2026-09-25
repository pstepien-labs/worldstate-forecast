# Etap 02 — Zbieranie faktów

Uruchamiany **cztery razy**, w osobnych sesjach: `G1`, `G2`, `G3`, `G4` (parametr z argumentu komendy). Grupy można uruchamiać w dowolnej kolejności.

## Zakres grup

- **G1 — MIL + INF:** Ukraina i wschodnia flanka NATO; Bałtyk; Morze Czarne; Bliski Wschód (działania zbrojne, Huti, Liban, Irak); Tajwan i Morze Płd.-chińskie; Półwysep Koreański; przesmyki: Ormuz, Bab al-Mandab i Morze Czerwone, Suez, Malakka, Bosfor i Dardanele, Panama, szlaki arktyczne, Cieśniny Duńskie. Obecność wojsk USA w Europie i w Polsce.
- **G2 — ENE + TEC:** ropa (ceny, podaż, zapasy, OPEC+, raport IEA), gaz i LNG (TTF, magazyny UE i PL, Katar, Norwegia, Jamał), paliwa w Polsce, nawozy i żywność, ziemie rzadkie, półprzewodniki i kontrola eksportu technologii, uran, metale krytyczne, komponenty wojskowe.
- **G3 — GOS + FIN:** cła, sankcje i kontrsankcje (OFAC, UE, Chiny), budżety mocarstw (Rosja, USA, Chiny), banki centralne (Fed, EBC, NBP, Bank Rosji, PBoC), waluty i płatności (dolar, juan, BRICS, SPFS), PLN i finanse publiczne Polski, programy SAFE i finansowanie Ukrainy.
- **G4 — DYP + WEW:** szczyty i rozmowy, sojusze i umowy, wybory i zmiany władzy, polityka wewnętrzna USA, Rosji, Chin i Iranu; Afryka (Sahel, Sudan, Róg Afryki); Ameryka Łacińska (Wenezuela, Kuba); Kaukaz; Azja Centralna; Arktyka polityczna (Grenlandia).

**Okres:** od `OKRES_OD` do `DATA_STANU` z `AKTUALNE.md`. Dla wydania 01: od 21.09.2026.

## Zadania

1. Przeczytaj z poprzedniego wydania fakty i blok stanu dla tej grupy — to punkt wyjścia. Szukaj zmian, nie przepisuj starego obrazu.
2. Priorytet mają obszary z `00_plan.md` i zdarzenia związane z PIR. Dla każdego obszaru — co najmniej dwa niezależne źródła.
3. Zdarzenia kluczowe: trzy perspektywy (Z, A, T). Szukaj w języku aktora (RU, ZH, AR, FA, TR), korzystając z `zrodla/mapa_zrodel.md`. Brak perspektywy zapisz jako lukę.
4. Zapisuj rekordy faktów w tabeli według metodologii §9. Deklaracje (DEKL) oddzielaj od wykonanych działań (WYK).
5. Wartości wskaźników bloku L należących do grupy — każda z datą i źródłem:
   - G1: przepływy przez Ormuz (IMF PortWatch), status Bab al-Mandab i Suezu, linia frontu, lotniskowce USA w Indo-Pacyfiku, wojska USA w PL, ostatni art. 4;
   - G2: Brent, TTF, magazyny UE i PL, cena diesla w PL, status zawieszenia kontroli ziem rzadkich;
   - G3: deficyt Rosji, stopy EBC, NBP i Fed, cła USA na Chiny i UE, kurs EUR/PLN;
   - G4: status rozmów pokojowych, status Iranu, Wenezueli, Sahelu i Kaukazu, ostatni szczyt BRICS.
6. Sekcja **„Zmiany od poprzedniego wydania”**: co nowego, co się potwierdziło bez zmian (z datą potwierdzenia), co przestało być aktualne i dlaczego.
7. Sekcja **„Luki i sprzeczności”** (materiał do sekcji J raportu).
8. Sekcja **„Kandydaci na pytania”**: 5–15 propozycji pytań swobodnych z kryterium rozstrzygnięcia, źródłem i terminem. Bez prawdopodobieństw.
9. Nowe źródła dopisz do `rejestr/zrodla.csv`.

## Punkty kontrolne

Zapisuj plik `02_fakty/<GRUPA>.md` po każdym obszarze. Gdy kończy się budżet: zapisz stan, dopisz do `dziennik.md` wiersz „<GRUPA> niepełne: brakuje …” i zakończ. Ponowne uruchomienie tej samej grupy kontynuuje od braków.

**Budżet orientacyjny:** 40–80 wyszukiwań i pobrań na grupę.

## Zakazy

Żadnych prawdopodobieństw liczbowych. Żadnych wejść na domeny z listy w CLAUDE.md p. 9.

**Dziennik:** wpis etapu w `dziennik.md` podaje godzinę rozpoczęcia i zakończenia etapu (dd.mm.rrrr gg:mm).

Commit: `wydanie-NN etap-02-<GRUPA>`.
