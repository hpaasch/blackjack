# receives cards
# calculates value of cards
# assesses whether to hit or stay

# collaborates with Dealer, Cards, Hand

# import random
from deck import Deck


class Player:

    # player shows up with $100 and an empty hand
    def __init__(self):
        # self.player = Player()
        # self.dealer = Player()
        self.deck = Deck()
        self.wallet = 100
        self.hand_total = 0
        # self.cards_in_hand = Deck.hand

    def hold_cards(self):
        self.hand_total = self.deck.value_the_cards()
        return self.hand_total


# hep_test = Player()
# hep_test.get_card()
# print("Buckaroos: ", hep_test.wallet)
# print("Hand's current total: ", hep_test.deck.value_the_cards())




