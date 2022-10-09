from blackjack.cards import *


# test if we can add two cards together, which should yield a Cards object
def test_add_two_cards():
    pass


# test if we can create and shuffle a deck of cards
def test_shuffle_deck():
    # creates a brand new card deck
    deck = Deck()
    assert len(deck) == 52

    # shuffles the deck and checks that it is different from the unshuffled deck
    unshuffled_deck = deck.copy()
    deck.shuffle()
    assert deck != unshuffled_deck