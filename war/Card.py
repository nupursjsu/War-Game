from enum import Enum


class Suite(Enum):
    SPADE = '♠'
    HEART = '♥'
    CLUB = '♣'
    DIAMOND = '♦'


class Card:

    rankdict = {}

    def __init__(self, suite, value):
        if len(self.rankdict) == 0:
            self.__populateRank__()
        self.suite = suite
        self.value = value

    @classmethod
    def __populateRank__(cls):
        cls.rankdict = {}
        for i in range(2, 11):
            cls.rankdict[i] = i
        cls.rankdict['J'] = 11
        cls.rankdict['Q'] = 12
        cls.rankdict['K'] = 13
        cls.rankdict['A'] = 14

    # Suite plays no part in deciding rank of the cards
    def __cmp__(self, other):
        return self.rankdict[self.value] - self.rankdict[other.value]

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "(" + str(self.value) + "/" + str(self.suite.value) + ")"
