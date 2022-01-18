from war.Deck import Deck


class Player:

    def __init__(self, name, deck: Deck):
        self.name = name
        self.deck = deck

    def cardCount(self):
        return len(self.deck)

    def playCard(self):
        return self.deck.top()

    def offerWarPile(self):
        pile = []
        if len(self.deck) >= 3:
            for i in range(3):
                pile.append(self.deck.top())
        else:
            while len(self.deck) > 0:
                pile.append(self.deck.top())
        return pile