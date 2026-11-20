"""P-0038: the keyword concepts in sources/harvest/keywords.csv route the topics that L1/L4 found
"collected but not used" and no longer match the known false positives."""
import unittest

from tools.harvester.digest import Matcher


class KeywordConceptTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = Matcher()

    def has(self, text, concept):
        self.assertIn(concept, self.m.match(text), text)

    def lacks(self, text, concept):
        self.assertNotIn(concept, self.m.match(text), text)

    def test_swift_only_as_payment_system(self):
        self.lacks('Taylor Swift announces a new tour', 'currencies_payments')
        self.lacks('The ministry acted swiftly', 'currencies_payments')
        self.has('Iranian banks cut off from SWIFT', 'currencies_payments')
        self.has('Russia offers an alternative to the SWIFT network', 'currencies_payments')

    def test_polish_rule_of_law(self):
        self.has('Trybunał Konstytucyjny orzekł w sprawie ustawy', 'pl_rule_of_law')
        self.has('Prezydent zawetował ustawę o KRS', 'pl_rule_of_law')
        self.has('Poland: the presidential veto blocks the reform', 'pl_rule_of_law')

    def test_western_balkans_and_resignation(self):
        self.has('Vučić resigns, Serbia heads for a snap election', 'western_balkans')
        self.has('Vučić resigns, Serbia heads for a snap election', 'elections')
        self.has('Dodik and the Republika Srpska referendum', 'western_balkans')

    def test_sabotage_espionage(self):
        self.has('Former BND chief arrested on suspicion of espionage', 'sabotage_espionage')
        self.has('GRU-ordered arson attack foiled in Estonia', 'sabotage_espionage')
        self.has('Zatrzymano szpiega pracującego dla Rosji', 'sabotage_espionage')

    def test_lng_contracts_and_qatar_without_first_names(self):
        self.has('QatarEnergy declares force majeure on LNG cargoes', 'gas_lng')
        self.has('Orlen rozwiązuje kontrakt LNG z Katarem', 'gas_lng')
        self.lacks('Katarzyna Nowak wygrała turniej', 'gas_lng')

    def test_elections_in_more_languages(self):
        self.has('סקר: הליכוד מוביל לקראת הבחירות', 'elections')
        self.has('انتخابات مجلس الشورى', 'elections')
        self.has('Вибори в Україні після війни', 'elections')
        self.has('台湾地方选举结果', 'elections')

    def test_brazil_names_alone_are_not_elections(self):
        self.lacks('Lula visita Pequim e encontra Xi', 'elections')
        self.has('Lula vence o segundo turno', 'elections')

    def test_russia_domestic_repression_terms(self):
        self.has('Moscow court jails a foreign agent journalist', 'russia_domestic')
        self.has('Губернатор арестован по делу о госизмене', 'russia_domestic')
        self.lacks('Governor arrested in Ohio over fraud', 'russia_domestic')


if __name__ == '__main__':
    unittest.main()
