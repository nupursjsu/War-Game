import unittest

from war.Card import spade, club, heart
from war.Deck import Deck
from war.Player import Player


class PlayerTestCase(unittest.TestCase):

    def test_cardcount(self):
        deck = Deck([spade(8), club(2), club('A'), spade(3), heart(10)])
        self.assertEqual(5, Player("Jenny", deck).cardCount())

    def test_offerWarPile_with_size_greater_than_3(self):
        deck = Deck([spade(8), club(2), club('A'), spade(3), heart(10)])
        player = Player("Jenny", deck)
        self.assertEqual(3, len(player.offerWarPile()))
        self.assertEqual(2, player.cardCount())

    def test_offerWarPile_with_size_less_than_3(self):
        deck = Deck([spade(8), club(2)])
        player = Player("Jenny", deck)
        self.assertEqual(2, len(player.offerWarPile()))
        self.assertEqual(0, player.cardCount())
