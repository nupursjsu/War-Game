import unittest
from war.Card import Card, Suite


class CardTestCase(unittest.TestCase):
    def test_cmp_operators(self):
        card1 = Card(Suite.SPADE, 8)
        card2 = Card(Suite.HEART, 9)
        card3 = Card(Suite.DIAMOND, 8)
        self.assertTrue(card1 < card2)
        self.assertTrue(card1 <= card3)
        self.assertTrue(card1 == card3)
        self.assertTrue(card1 != card2)
        self.assertTrue(card2 >= card3)
        self.assertTrue(card2 >= card3)
        self.assertFalse(card1 != card3)

    def test_str(self):
        self.assertEquals("(8/♠)", str(Card(Suite.SPADE, 8)))

if __name__ == '__main__':
    unittest.main()
