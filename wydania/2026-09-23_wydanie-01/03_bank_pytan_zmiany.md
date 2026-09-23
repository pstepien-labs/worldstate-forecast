# Etap 03 — Zmiany w banku pytań (wydanie 01, stan 23.09.2026)

Wydanie 01 ustala panel stały (metodologia §3.1) i dodaje pierwsze pytania swobodne. Rejestr przed etapem: 0 pytań. Po etapie: **73 pytania AKTYWNE** (Q-0001…Q-0073) — panel 40 (5 × 8 wektorów), swobodne 33. Bez prognoz.

## 1. Zasady zastosowane w tym wydaniu

**Data utworzenia** wszystkich pytań: 23.09.2026. Każde kryterium dotyczy zdarzeń po 23.09.2026 (zwykle „między 24.09 a …”), więc wydarzenia 23.09 (Rubio–Ławrow, wystąpienia w ONZ) i 24.09 (szczyt Xi–Trump) są albo poza pytaniami, albo są ich przedmiotem.

**Termin pytań krótkich:** 07.10.2026 — orientacyjna data wydania 02 (00_plan §1, do potwierdzenia przez użytkownika). Pytania „kroczące” w panelu (Q-0006, Q-0013, Q-0014, Q-0025, Q-0037) po rozstrzygnięciu zastępuje się analogicznym pytaniem z tego samego wektora i klastra z nową datą (§3.1).

**Stosowanie §3.5 (p_status_quo) — reguły mechaniczne użyte konsekwentnie:**
1. TAK wymaga nowego działania aktora (dekret, uderzenie, atak, wpis na listę, ogłoszenie, podpis, porozumienie, zmiana stopy) → **0.10**. Dotyczy także zdarzeń powtarzalnych (np. starty KRLD): bez nowej decyzji nie zajdą.
2. Progi dla wielkości ciągłych (ceny, kursy, magazyny, indeksy): TAK po tej samej stronie progu co ostatnia znana wartość → 0.90; po przeciwnej → **0.10**. Wszystkie progi w tym wydaniu leżą po przeciwnej stronie ostatniej wartości, więc 0.10. Trend (np. tłoczenie gazu) nie jest „stanem” — liczy się poziom.
3. Wybory: TAK = urzędujący zachowuje urząd lub większość → **0.90** (Q-0031, Q-0033); pytania o nowy układ bez odpowiednika w stanie obecnym (największy klub w nowym Sejmie, wynik > 50% w I turze) → **0.50**.
4. Wartość bieżąca leży dokładnie na progu lub brak danych o stanie obecnym → **0.50** (Q-0047, Q-0053, Q-0054).
5. Termin z góry zaplanowanego wydarzenia bez wskazania kierunku (Q-0029 — udział Trumpa w APEC) → **0.50**.

Wynik: 65 × 0.10, 6 × 0.50, 2 × 0.90. Przewaga 0.10 wynika z konstrukcji pytań („czy coś się zmieni”), nie z oceny.

**czyj_sukces (§3.6):** wpisany tylko tam, gdzie TAK wyraźnie wzmacnia aktora kosztem innego; w razie wątpliwości BRAK. KOMPROMIS — dla pytań, w których TAK oznacza porozumienie przeciwników (rozejm, przedłużenie zawieszenia, traktat). Rozkład: BRAK 58, KOMPROMIS 7, ROSJA 3, UKRAINA 2, UE 1, CHINY 1, USA_ZACHOD 1. W sześciu propozycjach z 00 zmieniono czyj_sukces na BRAK (P-002, P-003, P-005, P-013, P-021, P-027) — uzasadnienie w uwagach pytań.

**Klastry (§3.4):** 43 etykiety. Stopy procentowe rozdzielono na STOPY_PL, STOPY_EBC, STOPY_FED i STOPY_RU, bo decyzje różnych banków centralnych nie są tym samym rozstrzygnięciem. Nowe etykiety spoza przykładów §3.4 (lista przykładowa): PALIWA_PL, PL_INFLACJA, PL_FINANSE, PLN, ZYWNOSC, OPEC, USA_UE_HANDEL, USA_CHINY_TECH, USA_CHINY_SZCZYTY, RU_SANKCJE_USA, RU_SANKCJE_UE, RU_WEW, IRAN_WOJNA, IRAN_WLADZA, KOREA, PANAMA, BALTYK_INFRA, BRAZYLIA_WYBORY, LOTWA_WYBORY, KAUKAZ, UA_USA, UA_FINANSOWANIE.

**Pomiar Ormuzu.** Pytania Q-0036 i Q-0037 rozstrzyga IMF PortWatch (AIS). Seria może nie obejmować ruchu eskortowanego bez transponderów (sprzeczność G1-001 vs G2-006; 03_analiza §1.1 C). Kryterium zostaje, bo jest jednoznaczne i publiczne; zastrzeżenie jest w uwagach pytań.

**Ropa — źródło.** Propozycje z 00 i kandydaci G2 wskazywali serię EIA RBRTE (spot). Pytania Q-0006–Q-0008 używają kontraktu ICE Brent front-month, bo stan odniesienia (99,25 USD, 22.09) dotyczy futures, a spot Dated Brent odbiegał od nich o kilkanaście USD (IEA: 113,48 USD 09.09, G2-010) — przy EIA próg nie miałby jasnego odniesienia do stanu obecnego.

## 2. Nowe pytania

### 2.1 Panel stały (40)

| ID | Wektor | Klaster | Pytanie | Termin | p_sq | czyj_sukces | PIR |
|---|---|---|---|---|---|---|---|
| Q-0001 | MIL | RU_MOBILIZACJA | Czy do 31.12.2026 prezydent Rosji podpisze dekret ogłaszający mobilizację (powszechną lub częściową)? | 31.12.2026 | 0.10 | BRAK | PIR-1 |
| Q-0002 | MIL | FLANKA | Czy do 31.12.2026 na terytorium państwa NATO zginie co najmniej jedna osoba w wyniku uderzenia rosyjskiego drona lub pocisku? | 31.12.2026 | 0.10 | BRAK | PIR-1; PIR-2 |
| Q-0003 | MIL | USA_EUROPA | Czy do 31.03.2027 Pentagon lub Biały Dom ogłosi decyzję o zmniejszeniu liczby żołnierzy USA w Europie o co najmniej 10 000? | 31.03.2027 | 0.10 | ROSJA | PIR-2 |
| Q-0004 | MIL | UA_FRONT | Czy według DeepState netto przyrost terytorium Ukrainy zajętego przez Rosję w październiku 2026 r. przekroczy 200 km²? | 31.10.2026 | 0.10 | ROSJA | PIR-1 |
| Q-0005 | MIL | TAJWAN | Czy do 31.03.2027 Dowództwo Teatru Wschodniego ChRL ogłosi nazwane ćwiczenia wojskowe wokół Tajwanu? | 31.03.2027 | 0.10 | BRAK | PIR-4 |
| Q-0006 | ENE | ROPA_CENA | Czy cena rozliczeniowa kontraktu ICE Brent front-month w dniu 06.10.2026 przekroczy 100,00 USD/bbl? | 06.10.2026 | 0.10 | BRAK | PIR-3; PIR-5 |
| Q-0007 | ENE | ROPA_CENA | Czy cena rozliczeniowa kontraktu ICE Brent front-month przekroczy 120 USD/bbl w dowolnym dniu sesyjnym między 24.09 a 31.12.2026? | 31.12.2026 | 0.10 | BRAK | PIR-3; PIR-5 |
| Q-0008 | ENE | ROPA_CENA | Czy cena rozliczeniowa kontraktu ICE Brent front-month spadnie poniżej 80 USD/bbl w dowolnym dniu sesyjnym między 24.09 a 31.12.2026? | 31.12.2026 | 0.10 | BRAK | PIR-3; PIR-5 |
| Q-0009 | ENE | ENERGIA_UE | Czy cena rozliczeniowa kontraktu TTF front-month przekroczy 90 EUR/MWh w dowolnym dniu sesyjnym między 24.09 a 31.12.2026? | 31.12.2026 | 0.10 | BRAK | PIR-3 |
| Q-0010 | ENE | ENERGIA_UE | Czy zapełnienie magazynów gazu w UE według GIE AGSI+ w dniu gazowym 01.01.2027 będzie niższe niż 55,0%? | 01.01.2027 | 0.10 | BRAK | PIR-3 |
| Q-0011 | GOS | USA_CHINY_HANDEL | Czy do 10.11.2026 rządy USA i ChRL obydwa ogłoszą przedłużenie rozejmu handlowego (celnego) albo nowe porozumienie handlowe, które go zastępuje? | 10.11.2026 | 0.10 | KOMPROMIS | PIR-4 |
| Q-0012 | GOS | RU_SANKCJE_USA | Czy do 31.12.2026 prezydent USA nałoży cło na podstawie ustawy H.R. 5334 na towary z co najmniej jednego państwa innego niż Rosja? | 31.12.2026 | 0.10 | BRAK | PIR-1; PIR-4; PIR-6 |
| Q-0013 | GOS | PL_INFLACJA | Czy szybki szacunek GUS inflacji CPI za wrzesień 2026 r. wyniesie co najmniej 3,5% r/r? | 30.09.2026 | 0.10 | BRAK | PIR-6; PIR-3 |
| Q-0014 | GOS | ZYWNOSC | Czy indeks cen żywności FAO (FFPI) za wrzesień 2026 r. będzie wyższy niż 133,3 pkt? | 09.10.2026 | 0.10 | BRAK | PIR-3 |
| Q-0015 | GOS | USA_UE_HANDEL | Czy do 31.03.2027 USA wprowadzą cło na towary z UE przekraczające pułap 15% ustalony w porozumieniu z 2026 r.? | 31.03.2027 | 0.10 | BRAK | PIR-6 |
| Q-0016 | FIN | STOPY_PL | Czy RPP zmieni stopę referencyjną NBP na którymkolwiek posiedzeniu między 24.09 a 31.12.2026? | 31.12.2026 | 0.10 | BRAK | PIR-6 |
| Q-0017 | FIN | STOPY_EBC | Czy EBC podniesie stopę depozytową na posiedzeniu odbytym między 24.09 a 31.12.2026? | 31.12.2026 | 0.10 | BRAK | PIR-6 |
| Q-0018 | FIN | CN_SANKCJE_WTORNE | Czy do 31.03.2027 OFAC wpisze na listę SDN bank zarejestrowany w ChRL kontynentalnej w związku z Iranem lub Rosją? | 31.03.2027 | 0.10 | BRAK | PIR-4; PIR-5; PIR-6 |
| Q-0019 | FIN | RU_SANKCJE_UE | Czy do 31.12.2026 Rada UE przyjmie 22. pakiet sankcji wobec Rosji? | 31.12.2026 | 0.10 | UE | PIR-1; PIR-6 |
| Q-0020 | FIN | STOPY_RU | Czy Bank Rosji obniży stopę kluczową na posiedzeniu zaplanowanym na 23.10.2026? | 23.10.2026 | 0.10 | BRAK | PIR-1; PIR-6 |
| Q-0021 | TEC | CN_ZIEMIE_RZADKIE | Czy do 10.11.2026 ChRL ogłosi przedłużenie lub uchylenie zawieszenia kontroli eksportu ziem rzadkich wprowadzonych 09.10.2025? | 10.11.2026 | 0.10 | KOMPROMIS | PIR-4 |
| Q-0022 | TEC | CN_ZIEMIE_RZADKIE | Czy do 27.11.2026 ChRL ogłosi przedłużenie lub uchylenie zawieszenia zakazu eksportu galu, germanu, antymonu i materiałów supertwardych do USA? | 27.11.2026 | 0.10 | KOMPROMIS | PIR-4 |
| Q-0023 | TEC | USA_CHINY_TECH | Czy między 24.09 a 31.12.2026 MOFCOM wpisze co najmniej jeden podmiot z USA na listę kontroli eksportu lub na listę podmiotów niewiarygodnych? | 31.12.2026 | 0.10 | BRAK | PIR-4 |
| Q-0024 | TEC | USA_CHINY_TECH | Czy do 31.12.2026 rząd USA zezwoli na eksport do ChRL układów AI Nvidia z architekturą Blackwell lub nowszą? | 31.12.2026 | 0.10 | CHINY | PIR-4 |
| Q-0025 | TEC | CN_ZIEMIE_RZADKIE | Czy eksport magnesów trwałych z ziem rzadkich z ChRL do USA we wrześniu 2026 r. przekroczy 512 t? | 20.10.2026 | 0.10 | BRAK | PIR-4 |
| Q-0026 | DYP | UA_ROZMOWY | Czy do 30.11.2026 odbędzie się trójstronne spotkanie delegacji rządowych USA, Ukrainy i Rosji? | 30.11.2026 | 0.10 | BRAK | PIR-1; PIR-7 |
| Q-0027 | DYP | FLANKA | Czy między 24.09 a 31.12.2026 którekolwiek państwo NATO złoży wniosek o konsultacje na podstawie art. 4 Traktatu Północnoatlantyckiego? | 31.12.2026 | 0.10 | BRAK | PIR-1; PIR-2 |
| Q-0028 | DYP | ORMUZ | Czy do 31.12.2026 USA i Iran ogłoszą zawarcie porozumienia (ramowego, tymczasowego lub końcowego) obejmującego otwarcie Cieśniny Ormuz? | 31.12.2026 | 0.10 | KOMPROMIS | PIR-5; PIR-3 |
| Q-0029 | DYP | USA_CHINY_SZCZYTY | Czy Donald Trump weźmie osobiście udział w spotkaniu przywódców APEC w Shenzhen (18–19.11.2026)? | 19.11.2026 | 0.50 | BRAK | PIR-4 |
| Q-0030 | DYP | UA_ROZMOWY | Czy do 31.03.2027 Władimir Putin i Donald Trump spotkają się osobiście? | 31.03.2027 | 0.10 | BRAK | PIR-1; PIR-2 |
| Q-0031 | WEW | USA_WYBORY | Czy Partia Republikańska zdobędzie co najmniej 218 mandatów w Izbie Reprezentantów w wyborach 03.11.2026? | 31.12.2026 | 0.90 | BRAK | PIR-2; PIR-7 |
| Q-0032 | WEW | IRAN_WLADZA | Czy do 31.12.2026 zostanie opublikowane nowe nagranie wideo lub audio z wystąpieniem Modżtaby Chameneiego? | 31.12.2026 | 0.10 | BRAK | PIR-5; PIR-7 |
| Q-0033 | WEW | BRAZYLIA_WYBORY | Czy Luiz Inácio Lula da Silva wygra wybory prezydenckie w Brazylii w 2026 r. (I tura 04.10 lub II tura 25.10)? | 31.10.2026 | 0.90 | BRAK | PIR-7 |
| Q-0034 | WEW | WENEZUELA | Czy do 31.03.2027 CNE lub rząd Wenezueli ogłosi konkretną datę wyborów prezydenckich? | 31.03.2027 | 0.10 | BRAK | PIR-7 |
| Q-0035 | WEW | SAHEL | Czy do 31.03.2027 Assimi Goïta przestanie sprawować władzę w Mali (zamach, rezygnacja, śmierć lub przejęcie Bamako przez JNIM lub FLA)? | 31.03.2027 | 0.10 | BRAK | PIR-7 |
| Q-0036 | INF | ORMUZ | Czy w dowolnym dniu między 24.09 a 31.12.2026 średnia 7-dniowa liczby przejść przez Cieśninę Ormuz według IMF PortWatch przekroczy 40 statków na dobę? | 31.12.2026 | 0.10 | BRAK | PIR-5; PIR-3 |
| Q-0037 | INF | ORMUZ | Czy IMF PortWatch odnotuje co najmniej 20 przejść przez Cieśninę Ormuz w dowolnej dobie między 24.09 a 07.10.2026? | 07.10.2026 | 0.10 | BRAK | PIR-5; PIR-3 |
| Q-0038 | INF | ORMUZ | Czy do 31.12.2026 USA oficjalnie zniosą lub zawieszą blokadę morską portów irańskich? | 31.12.2026 | 0.10 | BRAK | PIR-5 |
| Q-0039 | INF | PANAMA | Czy do 31.10.2026 Urząd Kanału Panamskiego podniesie dzienny limit przejść powyżej 32? | 31.10.2026 | 0.10 | BRAK | PIR-3 |
| Q-0040 | INF | BALTYK_INFRA | Czy do 31.03.2027 rząd lub prokuratura państwa nadbałtyckiego ogłosi uszkodzenie podmorskiego kabla lub rurociągu na Bałtyku wraz z postępowaniem w sprawie działania zewnętrznego? | 31.03.2027 | 0.10 | BRAK | PIR-1; PIR-3 |

### 2.2 Pytania swobodne (33)

| ID | Wektor | Klaster | Pytanie | Termin | p_sq | czyj_sukces | PIR |
|---|---|---|---|---|---|---|---|
| Q-0041 | MIL | IRAN_WOJNA | Czy między 24.09 a 07.10.2026 CENTCOM lub Pentagon ogłosi uderzenie sił USA na cel na lądowym terytorium Iranu? | 07.10.2026 | 0.10 | BRAK | PIR-5 |
| Q-0042 | DYP | ORMUZ | Czy między 24.09 a 07.10.2026 odbędzie się kolejna runda rozmów przedstawicieli rządów USA i Iranu (bezpośrednich lub pośrednich)? | 07.10.2026 | 0.10 | BRAK | PIR-5 |
| Q-0043 | MIL | BAB_EL_MANDAB | Czy między 24.09 a 07.10.2026 Arabia Saudyjska potwierdzi atak pociskiem lub dronem z Jemenu wymierzony w Rijad? | 07.10.2026 | 0.10 | BRAK | PIR-5; PIR-3 |
| Q-0044 | MIL | USA_EUROPA | Czy do 07.10.2026 rząd USA lub RP oficjalnie ogłosi lokalizację nowej stałej bazy armii USA w Polsce? | 07.10.2026 | 0.10 | BRAK | PIR-2 |
| Q-0045 | MIL | FLANKA | Czy między 24.09 a 07.10.2026 DO RSZ lub MON potwierdzi naruszenie polskiej przestrzeni powietrznej przez obiekt z kierunku Rosji lub Białorusi? | 07.10.2026 | 0.10 | BRAK | PIR-1 |
| Q-0046 | MIL | KOREA | Czy między 24.09 a 07.10.2026 KRLD wystrzeli pocisk balistyczny? | 07.10.2026 | 0.10 | BRAK | PIR-4 |
| Q-0047 | MIL | TAJWAN | Czy między 24.09 a 07.10.2026 MON Tajwanu wykaże w raporcie dobowym co najmniej 20 statków powietrznych PLA wokół Tajwanu? | 07.10.2026 | 0.50 | BRAK | PIR-4 |
| Q-0048 | ENE | ENERGIA_UE | Czy cena rozliczeniowa kontraktu TTF front-month w dniu 06.10.2026 przekroczy 75,00 EUR/MWh? | 06.10.2026 | 0.10 | BRAK | PIR-3 |
| Q-0049 | ENE | ENERGIA_UE | Czy zapełnienie magazynów gazu w UE według GIE AGSI+ w dniu gazowym 06.10.2026 przekroczy 73,0%? | 06.10.2026 | 0.10 | BRAK | PIR-3 |
| Q-0050 | ENE | PALIWA_PL | Czy średnia krajowa cena oleju napędowego w notowaniu tygodniowym e-petrol z 07.10.2026 przekroczy 9,00 zł/l? | 07.10.2026 | 0.10 | BRAK | PIR-3 |
| Q-0051 | ENE | OPEC | Czy na spotkaniu 04.10.2026 państwa OPEC+ prowadzące dobrowolne cięcia ogłoszą podwyższenie wymaganej produkcji na listopad 2026 r.? | 07.10.2026 | 0.10 | BRAK | PIR-3 |
| Q-0052 | FIN | PLN | Czy średni kurs EUR/PLN NBP z 07.10.2026 będzie wyższy niż 4,3500? | 07.10.2026 | 0.10 | BRAK | PIR-6 |
| Q-0053 | FIN | RU_FINANSE | Czy projekt ustawy o budżecie federalnym Rosji na 2027 r. wniesiony do Dumy do 07.10.2026 przewiduje deficyt co najmniej 2,0% PKB? | 07.10.2026 | 0.50 | BRAK | PIR-1; PIR-6 |
| Q-0054 | WEW | RU_WEW | Czy Sprawiedliwa Rosja uzyska co najmniej 5,00% głosów w ostatecznych wynikach wyborów do Dumy ogłoszonych przez CKW? | 30.09.2026 | 0.50 | BRAK | PIR-7 |
| Q-0055 | WEW | LOTWA_WYBORY | Czy Zjednoczona Lista (Apvienotais saraksts) zdobędzie najwięcej mandatów w wyborach do Sejmu Łotwy 03.10.2026? | 10.10.2026 | 0.50 | BRAK | PIR-7 |
| Q-0056 | WEW | BRAZYLIA_WYBORY | Czy Lula da Silva zdobędzie ponad 50% ważnych głosów w I turze wyborów prezydenckich 04.10.2026? | 05.10.2026 | 0.50 | BRAK | PIR-7 |
| Q-0057 | GOS | USA_CHINY_HANDEL | Czy między 24.09 a 07.10.2026 USA opublikują raport o nadmiernych mocach produkcyjnych rekomendujący cła na ChRL albo ogłoszą nową stawkę celną na towary z ChRL? | 07.10.2026 | 0.10 | BRAK | PIR-4 |
| Q-0058 | GOS | USA_CHINY_HANDEL | Czy do 07.10.2026 rządy USA i ChRL obydwa ogłoszą przedłużenie rozejmu handlowego (celnego) lub nowe porozumienie handlowe? | 07.10.2026 | 0.10 | KOMPROMIS | PIR-4 |
| Q-0059 | DYP | UA_ROZMOWY | Czy do 07.10.2026 Rosja i Ukraina obie oficjalnie potwierdzą obowiązujące porozumienie o wzajemnym wstrzymaniu uderzeń w infrastrukturę energetyczną? | 07.10.2026 | 0.10 | KOMPROMIS | PIR-1; PIR-3 |
| Q-0060 | FIN | CN_SANKCJE_WTORNE | Czy między 24.09 a 07.10.2026 OFAC wpisze na listę SDN podmiot z ChRL lub Hongkongu w związku z Iranem? | 07.10.2026 | 0.10 | BRAK | PIR-4; PIR-5 |
| Q-0061 | FIN | RU_SANKCJE_USA | Czy między 24.09 a 07.10.2026 OFAC wpisze na listę SDN nowy podmiot w związku z Rosją? | 07.10.2026 | 0.10 | BRAK | PIR-1; PIR-6 |
| Q-0062 | INF | BAB_EL_MANDAB | Czy między 24.09 a 07.10.2026 UKMTO lub JMIC poinformuje o ataku na statek handlowy w Morzu Czerwonym, Bab al-Mandab lub Zatoce Adeńskiej? | 07.10.2026 | 0.10 | BRAK | PIR-5; PIR-3 |
| Q-0063 | INF | ORMUZ | Czy między 24.09 a 07.10.2026 UKMTO lub JMIC potwierdzi trafienie statku handlowego w Zatoce Perskiej, Cieśninie Ormuz lub Zatoce Omańskiej? | 07.10.2026 | 0.10 | BRAK | PIR-5 |
| Q-0064 | DYP | UA_USA | Czy do 07.10.2026 USA i Ukraina podpiszą międzyrządową umowę o dronach? | 07.10.2026 | 0.10 | UKRAINA | PIR-1; PIR-2 |
| Q-0065 | MIL | IRAN_WOJNA | Czy do 31.12.2026 CENTCOM lub Pentagon ogłosi uderzenie sił USA na cel na lądowym terytorium Iranu? | 31.12.2026 | 0.10 | BRAK | PIR-5 |
| Q-0066 | FIN | STOPY_FED | Czy FOMC podniesie przedział docelowy stopy funduszy federalnych na posiedzeniu 27–28.10.2026? | 28.10.2026 | 0.10 | BRAK | PIR-6 |
| Q-0067 | ENE | ENERGIA_UE | Czy zapełnienie magazynów gazu w UE według GIE AGSI+ w dniu gazowym 01.11.2026 wyniesie co najmniej 80,0%? | 01.11.2026 | 0.10 | BRAK | PIR-3 |
| Q-0068 | MIL | BAB_EL_MANDAB | Czy do 31.12.2026 siły USA przeprowadzą uderzenie na cele Huti w Jemenie? | 31.12.2026 | 0.10 | BRAK | PIR-5; PIR-2 |
| Q-0069 | MIL | TAJWAN | Czy do 31.12.2026 DSCA notyfikuje Kongresowi sprzedaż uzbrojenia Tajwanowi o łącznej wartości co najmniej 1 mld USD? | 31.12.2026 | 0.10 | USA_ZACHOD | PIR-4 |
| Q-0070 | FIN | PL_FINANSE | Czy do 31.03.2027 Fitch lub S&P obniży długoterminowy rating Polski w walucie obcej? | 31.03.2027 | 0.10 | BRAK | PIR-6 |
| Q-0071 | FIN | UA_FINANSOWANIE | Czy do 30.06.2027 Rada UE przyjmie akt prawny umożliwiający wykorzystanie na rzecz Ukrainy samych zamrożonych aktywów Banku Rosji (nie tylko zysków nadzwyczajnych)? | 30.06.2027 | 0.10 | UKRAINA | PIR-1; PIR-6 |
| Q-0072 | DYP | KAUKAZ | Czy do 30.06.2027 Armenia i Azerbejdżan podpiszą traktat pokojowy? | 30.06.2027 | 0.10 | KOMPROMIS | PIR-7 |
| Q-0073 | MIL | UA_FRONT | Czy do 30.06.2027 ISW oceni, że siły rosyjskie przejęły kontrolę nad całym Kramatorskiem lub całym Słowiańskiem? | 30.06.2027 | 0.10 | ROSJA | PIR-1 |

## 3. Zastąpienia

Brak — to pierwsze wydanie z rejestrem; żadne pytanie panelu nie zostało jeszcze rozstrzygnięte.

## 4. Propozycje z wydania 00 — decyzje (28)

| Propozycja | Decyzja | Pytanie | Powód / zmiana |
|---|---|---|---|
| P-001 | Przyjęta z poprawką | Q-0021 | Połączona z K-G2-06; dodano „lub uchylenie”; doprecyzowano ogłoszenia MOFCOM |
| P-002 | Przyjęta z poprawką | Q-0018 | „Większościowy udział państwa ChRL” trudny do weryfikacji → „bank zarejestrowany w ChRL kontynentalnej”; dodano Rosję (H.R. 5334); termin 31.03.2027; czyj_sukces → BRAK |
| P-003 | Przyjęta | Q-0036 | czyj_sukces KOMPROMIS → BRAK; zastrzeżenie o AIS |
| **P-004** | **Odrzucona** | → Q-0028, Q-0042 | **Rozstrzygnięta przed datą utworzenia:** runda 22.09 potwierdzona przez obie strony (Witkoff — G4-006; rzecznik MSZ Iranu — G4-008). Zastąpiona pytaniem o porozumienie (panel) i o kolejną rundę (swobodne) |
| P-005 | Przyjęta | Q-0026 | czyj_sukces KOMPROMIS → BRAK (spotkanie nie jest porozumieniem) |
| P-006 | Przyjęta z poprawką | Q-0001 | Pobór w 2026 całoroczny (00_plan §2) — zawężono do dekretu ogłaszającego mobilizację; wykluczono zgrupowania rezerwy |
| P-007 | Przyjęta jako swobodna | Q-0069 | Wektor MIL w panelu ma pięć pytań o wyższym priorytecie PIR-1/PIR-2 |
| P-008 | Przyjęta z poprawką | Q-0010 | Próg 45% → 55% (przy projekcji ok. 78% na 01.11 próg 45% wymagałby zimy skrajnej — ryzyko trywialności, §3.8) |
| P-009 | Przyjęta z poprawką | Q-0009 | Próg 100 → 90 EUR/MWh (stan 71–74, szczyt IX 84); doprecyzowano źródło |
| P-010 | Przyjęta z poprawką | Q-0007 | Źródło: kontrakt ICE (spójność z Q-0006) |
| P-011 | Przyjęta z poprawką | Q-0008 | Jak P-010 |
| **P-012** | **Odrzucona** | — | **Rozstrzygnięta przed datą utworzenia:** restart rurociągu Wschód–Zachód 22.09 potwierdzony przez co najmniej dwa niezależne media (Reuters za 3 źródłami; Al Arabiya, Al Khaleej — G2-008), co spełnia kryterium propozycji. Wektor INF w panelu uzupełniono pytaniami Q-0038–Q-0040 |
| P-013 | Przyjęta | Q-0002 | czyj_sukces ROSJA → BRAK |
| P-014 | Przyjęta | Q-0027 | Bez zmian merytorycznych |
| P-015 | Przyjęta | Q-0016 | Okres od 24.09 |
| P-016 | Przyjęta z poprawką | Q-0017 | Podwyżka 10.09 zaszła przed datą utworzenia — pytanie dotyczy posiedzeń po 23.09 |
| P-017 | Przyjęta | Q-0031 | Doprecyzowano rozstrzygnięcie przy nierozstrzygniętych mandatach |
| **P-018** | **Odrzucona** | → Q-0003 | Kryterium niejednoznaczne: rotacje zmieniają się rutynowo, a „redukcja rotacyjnej obecności” nie ma publicznej miary; sygnały wskazują raczej na wzrost w PL. Zastąpiona pytaniem o decyzję redukcji ≥ 10 tys. w Europie |
| **P-019** | **Odrzucona** | → Q-0044 | Kryterium nieweryfikowalne: brak publicznej ewidencji stanów wojsk USA w PL, „dodatkowych w ramach zapowiedzi z 21.05” nie da się oddzielić od rotacji. Zastąpiona pytaniem o lokalizację bazy |
| P-020 | Przyjęta z poprawką | Q-0032 | Połączona z K4-15; nagranie musi być nowe (po 23.09) |
| P-021 | Przyjęta | Q-0029 | czyj_sukces KOMPROMIS → BRAK; doprecyzowano przypadek odwołania szczytu |
| P-022 | Przyjęta jako swobodna | Q-0073 | Termin 31.12 → 30.06.2027 (tempo ok. 150 km²/4 tyg. czyni termin 31.12 bliskim trywialności); w panelu UA_FRONT zastępuje ją Q-0004 (DeepState, miesięcznie) |
| P-023 | Przyjęta | Q-0019 | Bez zmian merytorycznych |
| P-024 | Przyjęta z poprawką | Q-0034 | Termin → 31.03.2027 (wymiana TSJ i CNE w toku) |
| P-025 | Przyjęta z poprawką | Q-0035 | Termin → 31.03.2027; przewodniczący junty wskazany z nazwiska |
| P-026 | Przyjęta jako swobodna, przeformułowana | Q-0053 | Próg 2,0% równy zapowiedzi „ok. 2%” (G3-019) → p_status_quo 0.50; próg „≥ 2,0%”; termin 07.10 (wniesienie ok. 29.09–01.10) |
| P-027 | Przyjęta z poprawką | Q-0005 | Termin → 31.03.2027; czyj_sukces CHINY → BRAK |
| P-028 | Przyjęta z poprawką | Q-0011 | Połączona z K3-03; termin → 10.11 (data wygaśnięcia rozejmu); wersja krótka Q-0058 |

## 5. Kandydaci z etapu 02 niewykorzystani (z powodem)

| Kandydat | Powód |
|---|---|
| G1 K11 (USS George Washington w Jokosuce do 31.12) | Zależny od klastra IRAN_WOJNA; niski związek z decyzjami do terminu |
| G1 K12 (ICBM KRLD do 31.12) | Wektor MIL już najliczniejszy (15); Korea pokryta pytaniem krótkim Q-0046 |
| G1 K14 (zestrzelenie obiektu nad RP do 31.12) | Silnie zależne od Q-0002 i Q-0045 (FLANKA) |
| K-G2-01, K-G2-02 | Zastąpione Q-0006, Q-0007 (kontrakt ICE zamiast EIA — §1) |
| K-G2-09 (pełna przepustowość E-W — komunikat oficjalny) | Kryterium „pełna przepustowość” niejednoznaczne; Aramco nie komentuje przepływów |
| K-G2-10 (siła wyższa Katar–Edison) | Zależne od ORMUZ; rozstrzyga komunikat jednej firmy |
| K-G2-11 (przedłużenie zakazu eksportu diesla w RU) | Przedłużenia są seryjne (precedensy IX 2026) — ryzyko trywialności (§3.8) |
| K-G2-13 (ponowne obniżenie VAT lub cena maksymalna paliw w PL) | Brak sygnału rządu (G2 §3: luka); do rozważenia w wydaniu 02 |
| K3-02 (cło z H.R. 5334 na Chiny) | Zawiera się w Q-0012; dublowałoby klaster |
| K3-05 (budżet RU w III czytaniu ≥ 2,0%) | Zastąpione wersją krótką Q-0053 (III czytanie po 30.11 dałoby NIE niezależnie od deficytu) |
| K3-08 (EBC 29.10), K3-09 (RPP 07.10) | Zawierają się w Q-0017 i Q-0016 |
| K4-06 (ratyfikacja umowy grenlandzkiej przez Inatsisartut) | Brak terminu posiedzenia; niski związek z PIR w horyzoncie |
| K4-10 (większość Demokratów w Izbie) | Dopełnienie Q-0031 — duplikat |
| K4-12 (data wyborów w Wenezueli) | = P-024 → Q-0034 |
| K4-13 (nowy skład TSJ w Wenezueli) | Zależne od klastra WENEZUELA; PIR-7 pokryty |

## 6. Statystyka

**Horyzonty (§3.3)** — termin liczony od daty utworzenia 23.09.2026:

| Horyzont | Panel | Swobodne | Razem | Udział | Cel §3.3 |
|---|---|---|---|---|---|
| Do następnego wydania (≤ 10.10.2026) | 4 | 24 | 28 | 38% | ok. 40% |
| Do końca kwartału (11.10–31.12.2026) | 27 | 5 | 32 | 44% | ok. 40% |
| Dłuższe (po 31.12.2026) | 9 | 4 | 13 | 18% | ok. 20% |

Uwaga: trzy pytania krótkie mają termin 09–10.10 (FAO, Łotwa, wyniki CVK) — w `wyniki.py` wpadną do przedziału „≤ 100 dni”, bo prognozy powstaną ok. 24–25.09.

**Wektory:**

| Wektor | Panel | Swobodne | Razem |
|---|---|---|---|
| MIL | 5 | 10 | 15 |
| ENE | 5 | 5 | 10 |
| GOS | 5 | 2 | 7 |
| FIN | 5 | 7 | 12 |
| TEC | 5 | 0 | 5 |
| DYP | 5 | 4 | 9 |
| WEW | 5 | 3 | 8 |
| INF | 5 | 2 | 7 |
| **Razem** | **40** | **33** | **73** |

**PIR (pytania mogą mieć kilka):** PIR-1 — 17, PIR-2 — 8, PIR-3 — 20, PIR-4 — 16, PIR-5 — 17, PIR-6 — 14, PIR-7 — 10. PIR-2 jest pokryty najsłabiej — kandydat do uzupełnienia w wydaniu 02.

**Klastry z największą liczbą pytań:** ORMUZ 6; ENERGIA_UE 5; po 3: FLANKA, TAJWAN, ROPA_CENA, USA_CHINY_HANDEL, CN_ZIEMIE_RZADKIE, UA_ROZMOWY, BAB_EL_MANDAB. Waga 1 na klaster (§8) ogranicza wpływ tych skupisk na wynik.

**Trywialność (§3.8):** nie da się jej ocenić przed prognozami. Ryzyko pytań bliskich 0 lub 1 zmniejszono, podnosząc lub obniżając progi z propozycji 00 (P-008, P-009, P-022) i odrzucając kandydatów z seryjnym przebiegiem (K-G2-11). Kontrola po etapie 06.

## 7. Uwagi dla kolejnych etapów

- Etap 04: pytania Q-0011, Q-0021, Q-0022, Q-0024, Q-0029, Q-0057, Q-0058, Q-0060 zależą od szczytu 24.09, który odbędzie się po dacie stanu. Soczewki prognozują bez znajomości jego wyniku, chyba że etap 04 uruchomiono po 24.09 — wtedy wynik szczytu jest nowym faktem (CLAUDE.md §1), który należy zweryfikować w sieci.
- Etap 01 wydania 02: pierwsze rozstrzygnięcia — Q-0013 (30.09), Q-0054 (30.09), Q-0056 (05.10), Q-0006 i Q-0048/Q-0049 (06.10), pozostałe krótkie 07–10.10. Dane PortWatch (Q-0037) i FAO (Q-0014) mogą wymagać odroczenia rozstrzygnięcia do publikacji.
- Data wydania 02 (07.10) nie została potwierdzona przez użytkownika; jeśli się zmieni, terminy pytań krótkich pozostają bez zmian (rejestr tylko do dopisywania).
