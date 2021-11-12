import json
import random

class Card:
    suits = ["Club", "Diamond", "Heart", "Spade"]
    symbols = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    symbol_values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

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

    def get_value(self):
        if self.symbol != "Ace":
            return Card.symbol_values[self.symbol]
        elif self.symbol == "Ace":
            return "1 or 11"
        # TODO: Add error message here
        
class Cards:
    def __init__(self, cards = [None]):
        self.cards = cards # list of card objects
        #self.value = sum([card for card in cards])

    def __repr__(self):
        cards = ""
        for card in self.cards:
            cards += card.__repr__() + " "
        return cards

    def __add__(self, item): # must be able to process card oject
        if isinstance(item, Card):
            self.cards.append(item)
        elif isinstance(item, Cards):
            self.cards += item.cards

    def shuffle(self):
        random.shuffle(self.cards)

    def take_card(self):
        return self.cards.pop()

    # def sort(): # to do

    def get_value(self):
        value = 0
        for card in self.cards:
            if card.symbol != "Ace":
                value += card.get_value()
            elif card.symbol == "Ace":
                value += 11
                # TODO: Add more logic here
        return value


class Player:
    def __init__(self):
        self.bet = 0
        self.cards = Cards()

    def place_bet(self, amount):
        self.bet = amount
    
    def hit(self):
        self.cards += Deck.take_card()
    
    def stand(self):
        pass

    def double_down(self):
        pass
    
    def split(self):
        pass

    def surrender(self):
        pass

class Dealer:
    pass

class Blackjack:
    def __repr__(self):
        return "Hello"


h2 = Card("Heart", "Two")

print(h2)

s2 = Card("Spade", "Two")

c3 = Card("Club", "Three")
print(s2)

ca = Card("Club", "Ace")
print(ca.get_value())
cards = h2 + s2
print(cards, cards.get_value())
cards + c3
cards + ca

print(cards, cards.get_value())


