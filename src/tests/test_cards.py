from blackjack.cards import *

def test_print():
    ace_spade_card = Card(Rank.ACE, Suit.SPADE)
    assert ace_spade_card.__repr__() == U"\U0001F0A1"


# test if we can add two cards together, which should yield a Cards object
def test_add_two_cards():
    ace_spade_card = Card(Rank.ACE, Suit.SPADE)
    eight_heart_card = Card(Rank.EIGHT, Suit.HEART)

    cut = ace_spade_card + eight_heart_card
    cards = U' '.join(map(str, [U"\U0001F0A1", U"\U0001F0B8"]))

    assert isinstance(cut, Cards)
    assert cut.__repr__() == cards
    assert len(cut) == 2


# test if we can create and shuffle a deck of cards
def test_shuffle_deck():
    # creates a brand new card deck
    deck = Deck()
    assert len(deck) == 52

    # shuffles the deck and checks that it is different from the unshuffled deck
    unshuffled_deck = deck.copy()
    deck.shuffle()
    assert deck != unshuffled_deck