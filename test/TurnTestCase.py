import unittest

from war.Card import Card, Suite
from war.Deck import Deck
from war.Player import Player
from war.Turn import Turn

class TurnTestCase(unittest.TestCase):
    def test_battle(self):
        number = 1
        playerDeck1 = Deck(Card(Suite.SPADE, 10))
        playerDeck2 = Deck(Card(Suite.DIAMOND, 8))
        player1 = Player("Rahul", playerDeck1)
        player2 = Player("Nupur", playerDeck2)
        turn = Turn(number, player1, player2)
        turn.start()
        self.assertEqual(0, turn.winner)
        self.assertEqual(False, turn.isWar)
        self.assertEqual(2, len(player1.deck))
        self.assertEqual(0, len(player2.deck))

    def test_war_with_2_battles(self):
        number = 2
        playerDeck1 = Deck([Card(Suite.SPADE, 8), Card(Suite.CLUB, 2), Card(Suite.CLUB, 'A'), Card(Suite.SPADE, 3), Card(Suite.HEART, 10)])
        playerDeck2 = Deck([Card(Suite.DIAMOND, 8), Card(Suite.CLUB, 3), Card(Suite.HEART, 'J'), Card(Suite.DIAMOND, 10), Card(Suite.SPADE, 5)])
        player1 = Player("Rahul", playerDeck1)
        player2 = Player("Nupur", playerDeck2)
        turn = Turn(number, player1, player2)
        turn.start()
        self.assertEqual(True, turn.isWar)
        self.assertEqual(0, turn.winner)
        self.assertEqual(10, len(player1.deck))
        self.assertEqual(0, len(player2.deck))

    def test_war_with_3_battles(self):
        number = 2
        playerDeck1 = Deck([Card(Suite.SPADE, 8), Card(Suite.CLUB, 2), Card(Suite.CLUB, 'A'), Card(Suite.SPADE, 3),
                            Card(Suite.HEART, 10), Card(Suite.SPADE, 6), Card(Suite.CLUB, 4), Card(Suite.DIAMOND, 2),
                           Card(Suite.DIAMOND, 3), Card(Suite.SPADE, 'A')])
        playerDeck2 = Deck([Card(Suite.DIAMOND, 8), Card(Suite.CLUB, 3), Card(Suite.HEART, 'J'), Card(Suite.DIAMOND, 10),
                            Card(Suite.SPADE, 10), Card(Suite.SPADE, 5), Card(Suite.CLUB, 5), Card(Suite.CLUB, 6),
                            Card(Suite.SPADE, 'J')])
        player1 = Player("Rahul", playerDeck1)
        player2 = Player("Nupur", playerDeck2)
        turn = Turn(number, player1, player2)
        turn.start()
        self.assertEqual(True, turn.isWar)
        self.assertEqual(1, turn.winner)
        self.assertEqual(1, len(player1.deck))
        self.assertEqual(18, len(player2.deck))


    def test_war_where_everyone_loses(self):
        number = 2
        playerDeck1 = Deck([Card(Suite.SPADE, 8), Card(Suite.CLUB, 2), Card(Suite.CLUB, 'A')])
        playerDeck2 = Deck([Card(Suite.DIAMOND, 8), Card(Suite.CLUB, 3)])
        player1 = Player("Rahul", playerDeck1)
        player2 = Player("Nupur", playerDeck2)
        turn = Turn(number, player1, player2)
        turn.start()
        self.assertEqual(True, turn.isWar)
        self.assertEqual(-1, turn.winner)
        self.assertEqual(0, len(player1.deck))
        self.assertEqual(0, len(player2.deck))


    def test_war_where_player_runs_out_of_resources(self):
        number = 2
        playerDeck1 = Deck([Card(Suite.SPADE, 8), Card(Suite.CLUB, 2), Card(Suite.CLUB, 'A'), Card(Suite.SPADE, 3),
                            Card(Suite.HEART, 10)])
        playerDeck2 = Deck([Card(Suite.DIAMOND, 8), Card(Suite.CLUB, 3), Card(Suite.HEART, 'J'), Card(Suite.DIAMOND, 10)])
        player1 = Player("Rahul", playerDeck1)
        player2 = Player("Nupur", playerDeck2)
        turn = Turn(number, player1, player2)
        turn.start()
        self.assertEqual(True, turn.isWar)
        self.assertEqual(0, turn.winner)
        self.assertEqual(9, len(player1.deck))
        self.assertEqual(0, len(player2.deck))


if __name__ == '__main__':
    unittest.main()