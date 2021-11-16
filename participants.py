from cards import *

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bet = 0
        self.cards = Cards()

    def place_bet(self, amount):
        if self.money < amount:
            print("Bet amount is too large.")
        self.bet = amount
        self.money -= amount
    
    def __repr__(self):
        return self.name + self.cards.__repr__()

    def stand(self):
        pass

    def double_down(self):
        pass
    
    def split(self):
        pass

    def surrender(self):
        pass

class Dealer:
    def __init__(self):
        self.name = "Dealer"
        self.cards = Cards()

    def deal_card(self, receiver, deck, face_down = False):
        card = deck.take_card()
        print("Dealing {card} to {receiver}".format(card = card.__repr__(), receiver = receiver.name))
        if isinstance(receiver, Dealer):
            if face_down == False:
                receiver.cards + card
            elif face_down == True:
                receiver.hidden = card
        elif isinstance(receiver, Player):     
            receiver.cards + card
        return

    def deal_cards(self, receivers, deck):
        for receiver in receivers:
            self.deal_card(receiver, deck)