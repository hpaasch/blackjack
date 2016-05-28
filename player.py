# receives cards
# calculates value of cards
# assesses whether to hit or stay

# collaborates with Dealer, Cards, Hand

# import random
from deck import Deck


class Player:

    def __init__(self):
        self.hand = []
        self.hand.value = []

    def get_card(self):
        card_value = deal_one()
        self.hand += card_value
        return self.hand







