import unittest

from war.Card import Card, Suite
from war.Deck import Deck
from war.Player import Player
from war.Turn import Turn

class PlayerTestCase(unittest.TestCase):
    def test_cardcount(self):
        deck = Deck([Card(Suite.SPADE, 8), Card(Suite.CLUB, 2), Card(Suite.CLUB, 'A'), Card(Suite.SPADE, 3),
                            Card(Suite.HEART, 10)])
        player = Player("Jenny", deck)
        self.assertEqual(5, player.cardCount())

    def test_offerWarPile_with_size_greater_than_3(self):
        deck = Deck([Card(Suite.SPADE, 8), Card(Suite.CLUB, 2), Card(Suite.CLUB, 'A'), Card(Suite.SPADE, 3),
                     Card(Suite.HEART, 10)])
        player = Player("Jenny", deck)
        self.assertEqual(3, len(player.offerWarPile()))

    def test_offerWarPile_with_size_less_than_3(self):
        deck = Deck([Card(Suite.SPADE, 8), Card(Suite.CLUB, 2)])
        player = Player("Jenny", deck)
        self.assertEqual(2, len(player.offerWarPile()))
