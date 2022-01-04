from blackjack.cards import Card, Cards, Deck


# test if we can add two cards together, which should yield a Cards object
def test_add_two_cards():
    h2 = Card("Heart", "Two")
    s2 = Card("Spade", "Two")
    c2 = Card("Club", "Two")
    cards = h2 + s2

    # adding two Card objects shall create a Cards object
    assert isinstance(cards, Cards)
    assert len(cards) == 2
    assert (cards.__repr__() == "H2 S2")

    # adding a card to cards
    cards + c2
    assert isinstance(cards, Cards)
    assert len(cards) == 3
    assert (cards.__repr__() == "H2 S2 C2")


# test if we can create and shuffle a deck of cards
def test_shuffle_deck():
    # creates a brand new card deck
    deck = Deck()
    assert len(deck) == 52

    # shuffles the deck and checks that it is different from the unshuffled deck
    unshuffled_deck = deck.copy()
    deck.shuffle()
    assert deck != unshuffled_deck