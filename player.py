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
        # self.deck = Deck()  # is this creating another deck? probably
        self.wallet = 100
        self.hand_total = 0  # self.deck.value_the_cards()
        # self.deal_in = self.deck.initial_deal()
        self.cards_in_hand = []

    # def hold_cards(self):
        # self.hand_total = self.deck.value_the_cards()
        # return self.hand_total

'''
hep_test = Player()
print("Player's bank holds: ", hep_test.wallet)
print("Initial deal: ", hep_test.deal_in)
print("Hand's current total: ", hep_test.deck.value_the_cards())
'''





