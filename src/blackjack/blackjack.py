from blackjack.cards import Deck, Suit, Rank
from blackjack.participants import Player, Dealer
import sys


class Blackjack:
    def __init__(self, players, dealer, deck):
        print("Welcome to Blackjack!")

        self.players = players
        self.dealer = dealer
        self.deck = deck

        deck.shuffle()


    def place_bets(self):
        for player in self.players:
            amount = float(input("%s, enter your bet: " % player.name))
            player.place_bet(amount)


    def win(self, winner, winnings = 1):
        if isinstance(winner, Dealer):
            print("The dealer won!")
            return

        if isinstance(winner, Player):
            winners = list(winner)
        elif isinstance(winner, list):
            winners = winner
        
        for winner in winners:
            print("{winner} won!".format(winner = winner.name))
            winner.credit += winnings * winner.bet
            self.players.pop(self.players.index(winner))


    def bust(self, loser):
        if isinstance(loser, Player):
            print("{loser} bust!".format(loser = loser.name))
            self.players.pop(self.players.index(loser))
        elif isinstance(loser, Dealer):
            print("The dealer busts!")


    def tie(self, player):
        print("{player} and the dealer are tied".format(player = player.name))


    def player_decision(self, player):
        choice = int(input("Do you want another card?\n1) Yes\n2) No\n"))
        
        if choice == 1:
            number_of_cards = int(input("How many cards? "))
            for _ in range(number_of_cards):
                self.dealer.deal_card(player, self.deck)
            
        return True
         

    def score(self, participant):
        score = 0
        aces = []

        # Adds the value of all non Ace cards to the participant's 
        # score.
        # Aces are added to a list to be counted later.
        for card in participant.cards:
            if card.is_ace():
                aces.append(card)
            elif card.is_ten_or_face():
                score += 10
            else:
                score += card.rank.value

        for ace in aces:
            if score + 11 < (21 - len(aces) - 1):
                score += 11
            else:
                score += 1

        return score


    def show_board(self):

        print(self.dealer)

        for player in self.players:
            print(player)

    def play_round(self):
        players = self.players
        dealer = self.dealer
        deck = self.deck


        # Players place their bets
        #self.place_bets()

        # Each player receives one card face up
        dealer.deal_cards(players, deck)
        # Dealer gets one card face up 
        dealer.deal_card(dealer, deck)
        # Each player receives one card face up 
        dealer.deal_cards(players, deck)
        # Dealer gets one card face down
        dealer.deal_card(dealer, deck, face_down=True)

        self.show_board()
        
        # Check if any player has 21, if he does, he wins 1.5x their bet. 
        for player in players:
            player_score = self.score(player)
            print(player_score)
            if player_score > 21:
                self.bust(player)
            elif player_score == 21:
                # The player is then done for the round
                self.win(player, 1.5)
        
        
        # Each remaining player is asked if they want more cards. 
        # One or more may be asked for. 
        for player in players:
            stay = False
            while stay is not True:
                stay = self.player_decision(player)
                player_score = self.score(player)
                if player_score > 21:
                    self.bust(player)
        # If they do not want more cards, they say stay. 
        # If they at any point score more than 21, they bust.
        
        # One each player has finished their choice, the dealer flips
        # up their face down card. 
        dealer.reveal_card()
        self.show_board()
        
        # If the dealers score is 16 or under, they have to take another card,
        # or if their score is 17 or higher, they have to stay their hand.
        # If the dealer busts, each remaining player receives 2x their bet.
        
        dealer_score = self.score(dealer)
        while dealer_score <= 16:
            print("Dealer score: ", dealer_score)
            
            dealer.deal_card(dealer, deck)
            dealer_score = self.score(dealer)
        
        self.show_board()
        dealer_score = self.score(dealer)

        if dealer_score > 21:
            self.win(players, 2)
            self.bust(dealer)
        elif dealer_score == 21:
            self.win(dealer)
            self.bust(players)
        # Assuming the dealer hasn't busted, the rest of the players cards
        # are evaluated. Only the one who has a higher hand than the dealer 
        # wins 2x their bet. 
        # Everyone else loses their initial bet. 
        #highest_scoring_player = None

        highest_scoring_player = None
        dealer_score = self.score(dealer)
        for player in players:
            player_score = self.score(player)
            if player_score > dealer_score:
                highest_scoring_player = player

        if isinstance(highest_scoring_player, Player):
            self.win(highest_scoring_player, 2)
        # Now another round can start.