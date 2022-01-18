import random

from war.Card import Card, Suite


class Deck():
    """
    init Deck with 52 cards (by default)
    OR init with the cards provided
    """
    def __init__(self, *args):
        if len(args) == 0:
            self.cards = self.fresh()
            self.shuffle()
        elif len(args) == 1:
            # Create deck with the card(s) provided
            if isinstance(args[0], list):
                self.cards = args[0]
            elif isinstance(args[0], Card):
                self.cards = [args[0]]
            else:
                raise Exception("Invalid input to init Deck", args[0])
        else:
            raise Exception("Invalid inputs to init Deck", args)

    def shuffle(self):
        random.shuffle(self.cards)
        return self

    """
        Prepare a fresh deck of cards
    """
    def fresh(self):
        cards = []
        for suite in Suite:
            for num in range(2, 11):
                cards.append(Card(suite, num))
            cards.append(Card(suite, 'J'))
            cards.append(Card(suite, 'Q'))
            cards.append(Card(suite, 'K'))
            cards.append(Card(suite, 'A'))
        return cards

    """
    Add a Card/[Card]/Deck to the current Deck
    """
    def __iadd__(self, other):
        if isinstance(other, list):
            self.cards += other
        elif isinstance(other, Card):
            self.cards.append(other)
        elif isinstance(other, Deck):
            self.cards.appendAll(other.cards)
        return self

    def top(self):
        return self.cards.pop(0)

    # length of the Deck
    def __len__(self):
        return len(self.cards)

    # Fixed split of 2
    def split(self):
        return [Deck(self.cards[:26]), Deck(self.cards[26:])]

    def __str__(self):
        summary = ""
        for card in self.cards:
            summary += str(card) + " "
        print(summary)
