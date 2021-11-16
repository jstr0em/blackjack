import json
import random

class Card:
    suits = ["Club", "Diamond", "Heart", "Spade"]
    symbols = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    # read file
    with open('faces.json', 'r') as myfile:
        data = myfile.read()

    # parse file
    faces = json.loads(data)

    def __init__(self, suit, symbol):
        self.suit = suit
        self.symbol = symbol

        return
    def __repr__(self):
        return Card.faces[self.suit][self.symbol]

    def __add__(self, item):
        if isinstance(item, Card):
            return Cards([self, item])

    def get_suit(self):
        return self.suit
    
    def get_symbol(self):
        return self.symbol

# TODO: Can this inherit list? Might be nice for refactoring.
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
            return self + item.cards

    def shuffle(self):
        random.shuffle(self.cards)

    def take_card(self):
        return self.cards.pop()

    # def sort(): # to do


class Deck(Cards):
    def __init__(self):
        self.cards = [Card(suit, symbol) for symbol in Card.symbols for suit in Card.suits]
