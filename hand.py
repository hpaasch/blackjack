# takes initial deal
# values cards
# takes additional cards

from deck import Deck
from deck import full_deck_valued


class Hand:

    def __init__(self):
        self.cards_in_hand = []
        self.deck = Deck()

    def initial_deal(self):
        new_cards = []
        for _ in range(2):
            new_cards = Deck.deal_one_card(self.deck)
            self.cards_in_hand.append(new_cards)
        # print(self.cards_in_hand)
        return new_cards

    def __str__(self):
        # print(' '.join(self.cards_in_hand))
        return ' '.join(self.cards_in_hand)

    def draw_a_card(self):
        new_card = Deck.deal_one_card(self.deck)
        self.cards_in_hand.append(new_card)
        # print(self.cards_in_hand)
        return new_card

    def value_the_cards(self):
        hand_valued = 0
        for card in self.cards_in_hand:
            hand_valued += (full_deck_valued[card])
        # need Ace logic here
        # hand_valued = sum(full_deck_valued[card] for card in self.cards_in_hand)
        # print(hand_valued)
        return hand_valued
