import unittest

from war.Card import Card, Suite, spade, diamond, club, heart
from war.Deck import Deck
from war.Player import Player
from war.Turn import Turn


class TurnTestCase(unittest.TestCase):

    """
    Start a turn with two set of cards
    """
    def turnWithDecks(self, cards1, cards2):
        player1 = Player("Jenny", Deck(cards1))
        player2 = Player("John", Deck(cards2))
        return Turn(1, player1, player2).start(), player1, player2

    def test_battle(self):
        turn, player1, player2 = self.turnWithDecks(spade(10), diamond(8))
        self.assertEqual(0, turn.winner)
        self.assertEqual(False, turn.isWar)
        self.assertEqual(2, len(player1.deck))
        self.assertEqual(0, len(player2.deck))

    def test_war_with_2_battles(self):
        cards1 = [spade(8), club(2), club('A'), spade(3), heart(10)]
        cards2 = [diamond(8), club(3), heart('J'), diamond(10), heart(5)]
        turn, player1, player2 = self.turnWithDecks(cards1, cards2)
        self.assertEqual(True, turn.isWar)
        self.assertEqual(0, turn.winner)
        self.assertEqual(10, len(player1.deck))
        self.assertEqual(0, len(player2.deck))

    def test_war_with_3_battles(self):
        cards1 = [spade(8), club(2), club('A'), spade(3),
                  heart(10), spade(6), club(4), diamond(2),
                  diamond(3), spade('A')]
        cards2 = [diamond(8), club(3), heart('J'), diamond(10),
                  spade(10), spade(5), club(5), club(6), spade('J')]
        turn, player1, player2 = self.turnWithDecks(cards1, cards2)
        self.assertEqual(True, turn.isWar)
        self.assertEqual(1, turn.winner)
        self.assertEqual(1, len(player1.deck))
        self.assertEqual(18, len(player2.deck))

    def test_war_where_everyone_loses(self):
        cards1 = [spade(8), club(2), club('A')]
        cards2 = [diamond(8), club(3)]
        turn, player1, player2 = self.turnWithDecks(cards1, cards2)
        self.assertEqual(True, turn.isWar)
        self.assertEqual(-1, turn.winner)
        self.assertEqual(0, len(player1.deck))
        self.assertEqual(0, len(player2.deck))

    def test_war_where_one_player_runs_out_of_resources(self):
        cards1 = [spade(8), club(2), club('A'), spade(3), heart(10)]
        cards2 = [diamond(8), club(3), heart('J'), diamond(10)]
        turn, player1, player2 = self.turnWithDecks(cards1, cards2)
        self.assertEqual(True, turn.isWar)
        self.assertEqual(0, turn.winner)
        self.assertEqual(9, len(player1.deck))
        self.assertEqual(0, len(player2.deck))


if __name__ == '__main__':
    unittest.main()
