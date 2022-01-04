# Win conditions
When player has cards > dealer but <= 21
or 
if you have 21 then you win 1.5 times your bet from the dealer. The player is also done for that round. 

A "blackjack", i.e. a 10 + Ace, trumps another 21 value of 3 or mroe cards. 

If a player and the dealer has the same value, it is a tie and the player does not lose his bet. 

# Lose conditions
If your points are > 21 you are out - "bust". The dealer takes your bet. 

# Game starts
1. Every player places a bet
2. Dealer gives each player 1 card "face up" (including the dealer
3. Dealer gives each player 1 more card "face up" (ecluding the dealer)
4. Dealer is dealt his 2nd card "face down", i.e. the other players cannot see it.
5. Each player is given a choice if they will take one or more cards - "a hit", or if they will "stay". 
6. When the dealer has gone around the table, the dealer and all the players reveal their cards. 
7. If anyone has <= 16, then the dealer or player has to take another card. 
8. If the dealer busts, all remaining players receive 2x of their bet. 
9. If the dealer doesn't bust, then only the players who have a higher value than the dealer receives 2x of their bet. The rest lose their initial bet. 

# Card values
Cards 2-10 have the same value as their face value (i.e. 8 is worth 8)
Jack, Queen, and King are worth 10 each 
Ace is worth either 1 or 11 

# Activity diagram
@startuml
start
:Each player places a bet;
:Dealer and each player is given a card "face up";
:Each player is dealt a second card "face up";
:Evaluate score;
:Dealer receives his second card "face down";
if (Each player is given a choice to ...) then (Hit)
    :Player requests and receives a specified\n(one or more) cards "face up";
else (Stay)
endif
:Evaluate score;
:Dealer reveals his second card;
if (Any player or the dealer has value less than 16?) then (Yes)
    :Player or dealer takes another card "face up";
endif
:Evaluate score;
@enduml

# Evaluating Score 
Method for evaluating if a player has won, is eliminated, or proceeds.
@startuml
start

if (Player value > 21)
    :Player busts;
    :Player loses bet;
else if (Dealer value > 21)
    :Dealer busts;
else
    :Continue;
    switch (Player value is...)
        case (Equal to 21)
endif
switch (Player value is...)
    case (Greater than 21)
        :Player busts;
        :Player loses bet;
    case (Equal to 21)
    case (Less than or equal to 21)
        switch (Dealer value is...)
            case (Greater than 21)
                :Dealer busts;
                :Players receive 1.5x their bet;
            case (Equal to 21)
                switch (Player value is...)
                    case (Equal to 21)
                        switch (Anyone has "Blackjack"?)
                            case (Only dealer)
                                :Player loses;
                                :Player loses their bet;
                            case (Only player)
                                :Player wins;
                                :Players receive 1.5x their bet;
                            case (Both or none)
                                :Tie;
                                :Player's bet returned;
                        endswitch
                endswitch
            case (Less than 21)
                switch (Player value is...)
                    case (Greater than dealer's)
                        :Player wins;
                        :Players receive 1.5x their bet;
                    case (Equal to dealer's)
                        :Tie;
                        :Player's bet returned;
                    case (Less than dealer's)
                        :Player loses;
                        :Player loses their bet;
                endswitch
        endswitch
endswitch
end
@enduml

# Class diagram
@startuml
class Card
class Cards
class Deck
class Player
class Dealer
class Blackjack

Card : suit
Card : symbol

Card : __repr__()
Card : __add__()

Cards : value

Cards : shuffle()
Cards : take_card()
Cards : sort()
Cards : __add__()


Cards "1" *-- "1.." Card : contains
Player "1" *-- "1" Cards : contains
Dealer "1" *-- "1" Cards : contains
Deck "1" *-- "1" Cards : contains

Blackjack "1" *-- "1" Dealer : contains
Blackjack "1" *-- "1.." Player : contains
Blackjack "1" *-- "1" Deck : contains

Player : hit()
Player : place_bet()
Player : surrender()
Player : stay()

Dealer : deal()
Dealer : hit()
@enduml