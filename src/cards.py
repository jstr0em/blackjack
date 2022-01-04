import json
import random


class Card:
    suits = ["Club", "Diamond", "Heart", "Spade"]
    symbols = [
        "Ace", "Two", "Three", "Four", 
        "Five", "Six", "Seven", "Eight", 
        "Nine", "Ten", "Jack", "Queen", 
        "King"
        ]

    # loads all the string representations of the cards
    with open('blackjack/faces.json', 'r') as myfile:
        data = myfile.read()
    faces = json.loads(data)


    def __init__(self, suit, symbol):
        self.suit = suit
        self.symbol = symbol


    def __repr__(self):
        return Card.faces[self.suit][self.symbol]


    def __add__(self, item):
        if isinstance(item, Card):
            return Cards([self, item])


    def get_suit(self):
        return self.suit
    

    def get_symbol(self):
        return self.symbol


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
    def __init__(self):
        # populates the deck with each unique card in a deck of cards (excluding jokers)
        Cards.__init__(
            self, [
            Card(suit, symbol) 
            for symbol in Card.symbols 
            for suit in Card.suits
            ]
            )
