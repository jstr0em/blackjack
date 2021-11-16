from pytest import *
from main import *


def add_cards():
    h2 = Card("Heart", "Two")
    s2 = Card("Spade", "Two")
    c2 = Card("Club", "Two")
    cards = h2 + s2
    empty_cards = Cards()
    #print(empty_cards)
    empty_cards + c2
    #print(empty_cards)
    cards + c2

    #print(cards)

    assert (cards.__repr__() == "H2 S2 C2") and (cards.get_value() == 6)

def generate_deck():
    deck = Deck()

    assert len(deck.cards) == 52

def take_card_test():
    deck = Deck()

    card = deck.take_card()
    return card, len(deck.cards)

def play_blackjack():
    player1 = Player("Jonathan", 100)
    player2 = Player("Michael", 200)
    dealer = Dealer()
    deck = Deck()

    blackjack = Blackjack([player1, player2], dealer, deck)
    
    blackjack.play()

#add_cards()
#generate_deck()
play_blackjack()
