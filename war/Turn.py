from war.Card import Card
from war.Player import Player


class Turn:
    # number, player1: Player, player2: Player):
    def __init__(self, *args):
        if len(args) == 3:
            self.number = args[0]
            self.players: [Player] = [args[1], args[2]]
            self.isWar = False
            self.warPile = []
            self.battles: [(Card, Card)] = []
            self.winner = -1
            self.loser = -1

    """
    Start the turn and let the players play!
    """
    def start(self):
        while self.notEnded():
            self.battles.append((self.players[0].playCard(), self.players[1].playCard()))
            card1 = self.battles[len(self.battles) - 1][0]
            card2 = self.battles[len(self.battles) - 1][1]
            if card1 < card2:
                self.winner = 1
                self.loser = 0
                break
            elif card1 > card2:
                self.winner = 0
                self.loser = 1
                break
            else:
                self.isWar = True
                self.warPile += self.players[0].offerWarPile()
                self.warPile += self.players[1].offerWarPile()
        self.declareWinner()
        # Summarize each turn and print it
        print(self.summarize())
        return self

    """
        In the unlikely event where players lost all their cards in the last war.
        There is no winner!
        @see #summarize
    """
    def declareWinner(self):
        if self.winner == -1:
            if self.players[0].cardCount() != self.players[1].cardCount():
                # Deciding the de-facto winner based on the cardCount if players' are unable to finish the last war
                self.winner = 0 if self.players[0].cardCount() > self.players[1].cardCount() else 1
                self.loser = 0 if self.winner == 1 else 1
        self.finishTurn()

    """
    Wraps up the turn by adding cards to the winner's (if there is one) deck 
    """
    def finishTurn(self):
        if self.winner != -1:
            # Finish the turn by adding the cards from battle and warPile to the winner's deck
            for battle in self.battles:
                self.players[self.winner].deck += battle[0]
                self.players[self.winner].deck += battle[1]
            self.players[self.winner].deck += self.warPile

    """
    """
    def notEnded(self):
        return self.players[0].cardCount() > 0 and self.players[1].cardCount() > 0

    def summarize(self):
        summary = "| " + str(self.number) + " | "
        summary += ("War" if self.isWar else "Battle") + " | "

        # winner name
        if self.winner != -1:
            summary +=  self.players[self.winner].name
        else:
            summary += " No winner"
        summary += " | "

        # Last Battle info (In case of No winners, we just display card of last battle in any order)
        lastBattle = self.battles[len(self.battles) - 1]
        winnerCard = lastBattle[0] if self.winner == 0 else lastBattle[1]
        loserCard = lastBattle[1] if self.winner == 0 else lastBattle[0]
        summary += str(winnerCard) + " vs " + str(loserCard) + " | "

        # cardCount info
        summary += str(self.players[self.winner].cardCount())
        summary += " vs " + str(self.players[self.loser].cardCount())
        summary += " | "

        return summary