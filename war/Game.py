from war.Deck import Deck
from war.Player import Player
from war.Turn import Turn


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turns: [Turn] = []
        self.current = 0

    def start(self):
        print("|Turn|State|Winner|LastBattle|Cards|")
        while self.notEnded():
            self.current += 1

            # To avoid Game to go infinitely
            if self.current > 1000:
                self.player1.deck.shuffle()
                self.player2.deck.shuffle()

            turn = Turn(self.current, self.player1, self.player2)
            self.turns.append(turn)
            turn.start()

        self.winner = self.player1 if self.player2.cardCount() == 0 else self.player2

    def notEnded(self):
        return self.player1.cardCount() > 0 and self.player2.cardCount() > 0

    def summarize(self):
        winner = self.turns[len(self.turns) - 1].winner
        print((player1.name if winner == 0 else player2.name) + " wins!!")


if __name__ == "__main__":
    deck = Deck()
    playerDecks = deck.split()
    # Additional Shuffle
    player1 = Player("Jenny", playerDecks[0].shuffle())
    player2 = Player("John", playerDecks[1].shuffle())
    game = Game(player1, player2)
    game.start()
    game.summarize()
