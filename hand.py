from player import Player

class Hand:

    def __init__(self):
        print("Time to play some blackjack.")
        self.player = Player()
        self.dealer = Player()
        print("Player is: ", self.player)
        print("Dealer is: ", self.dealer)
        print("Player's hand: ", self.player.hand)
        # deal two cards to each
        # total player cards and inquire about a hit

    def players_hand(self):
        while self.player.hand < 21:
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


    '''
    def play_again(self):
        play_on = input("Another hand? Y/n ").lower()
        if play_on == 'y':
            launch_game()
        else:
            # report who_won
            sys.exit()
    '''

# new_round = Hand()
# new_round.players_hand()
# new_round.dealers_hand()
