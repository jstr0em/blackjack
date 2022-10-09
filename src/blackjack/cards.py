import random
from enum import Enum


class Suit(Enum):
    SPADE = 'A'
    HEART = 'B'
    DIAMOND = 'C'
    CLUB = 'D'


class Rank(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 'A'
    KNIGHT = 'B'
    QUEEN = 'D'
    KING = 'E'

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


    def __repr__(self):
        unicode = "0001F0{suit}{rank}".format(suit = self.suit, rank = self.rank)
        return chr(int(unicode, base=16))


    def __add__(self, item):
        if isinstance(item, Card):
            return Cards([self, item])


    def get_suit(self):
        return self.suit
    

    def get_symbol(self):
        return self.symbol

    def is_ace(self):
        return self.rank is Rank.ACE


    def is_face(self):
        return self.rank is Rank.KNIGHT or Rank.QUEEN or Rank.KING

    def is_ten_or_face(self):
        return type(self.rank.value) is str


class Cards(list):
    def __init__(self, *args):
        list.__init__(self, *args)


    def __repr__(self):
        cards = ""
        for card in self:
            cards += card.__repr__() + " "

        return cards.rstrip()


    def __add__(self, item): # must be able to process card oject
        if isinstance(item, Card):
            return self.append(item)
        elif isinstance(item, Cards):
            return self + item

    # shuffles the deck of cards
    def shuffle(self):
        random.shuffle(self)

    # wrapper for "pop"
    def take_card(self):
        return self.pop()


class Deck(Cards):
    def __init__(self, number_of_decks = 1):
        # populates the deck with each unique card in a deck of cards (excluding jokers)
        Cards.__init__(
            self, [
            Card(suit, rank) 
            for rank in Rank 
            for suit in Suit
            ] * number_of_decks
            )
