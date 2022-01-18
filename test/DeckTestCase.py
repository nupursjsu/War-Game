import unittest
from war.Card import spade, diamond, heart
from war.Deck import Deck


class DeckTestCase(unittest.TestCase):
    def test_len_and_init(self):
        # init full deck by default
        deck = Deck()
        self.assertEqual(52, len(deck))
        self.assertEqual(len(deck), len(deck.cards))

        # init with only one card (useful for testing)
        deck = Deck(spade(8))
        self.assertEqual(1, len(deck))
        self.assertEqual(len(deck), len(deck.cards))

        # init with list of cards (to give to players)
        deck = Deck([spade(8), diamond(8)])
        self.assertEqual(2, len(deck))
        self.assertEqual(len(deck), len(deck.cards))

    def test_add_assign_operator(self):
        deck = Deck(spade(8))
        self.assertEqual(1, len(deck))

        deck += heart(9)
        self.assertEqual(2, len(deck))


if __name__ == '__main__':
    unittest.main()
