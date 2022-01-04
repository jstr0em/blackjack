from blackjack.cards import *

class Player:
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit
        self.bet = 0
        self.cards = Cards()

    def place_bet(self, amount):
        if self.credit < amount:
            print("Bet amount is too large.")
        self.bet = amount
        self.credit -= amount
    
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


    # Lets the dealer deal a card to a receiver from a deck.
    # Optionally, the card can be dealt "face down", i.e. hidden. 
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


    def deal_cards(self, receivers, deck):
        for receiver in receivers:
            self.deal_card(receiver, deck)

    def reveal_card(self):
        self.cards + self.hidden
        self.hidden = None