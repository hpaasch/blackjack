from player import Player
from deck import Deck


class Hand:

    def __init__(self):
        self.player = Player()
        self.dealer = Player()
        # print("Player is: ", self.player)
        # print("Dealer is: ", self.dealer)
        print(">" * 40)
        # print("Player's hand: ", self.player.hand)

    def initial_deal(self):
        # self.player.hand = self.initial_deal()
        pass  # deal two cards to each

    def players_hand(self):
        while self.player.hand_total < 21:
            hit = input("Hit or Stay? H/S ").lower()
            if hit == 'h':
                Player.get_card(self.player)
                print("Player's hand: ", self.player.hand)
                if self.player.hand > 21:
                    print("Player's hand is a bust.")
            else:
                print("Player's hand: ", self.player.hand)
                break
        player_total = self.player.hand
        return player_total

    def dealers_hand(self):
        while self.dealer.hand < 17:
            Player.get_card(self.dealer)
        if self.dealer.hand > 21:
            print("Dealer's hand is bust at {}.".format(self.dealer.hand))
        else:
            print("Dealer's hand: ", self.dealer.hand)
        dealer_total = self.dealer.hand
        return dealer_total

hep_test = Hand()
# print(hep_test.players_hand())
