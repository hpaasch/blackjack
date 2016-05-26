# the master class
#
# holds value of multiple cards
# evaluated for win/lose/hit/stay

# collaborates with cards, player, dealer

from player import Player

class Hand:

    def __init__(self):
        print("Time to play some blackjack.")
        self.player = Player()
        self.dealer = Player()

    def players_hand(self):
        while self.hand < 21:
            hit = input("Another card? Y/n").lower()
            if hit == 'y':
                Player.get_card()
            else:
                break

    def dealers_hand(self):
        while self.hand < 17:
            Player.get_card()

    def play_again(self):
        pass

new_round = Hand()
print("Player is: ", new_round.player)

# print("Hope's hand: ", hep_player.hand)
# print("Dealer's hand: ", joe_dealer.hand)
