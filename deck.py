# defines possible cards to play
# shuffles
# delivers cards

from itertools import product
from random import sample

# possibly move cards to their own class?

suit = "CSHD"
rank = "A23456789TJQK"

full_deck = tuple(''.join(card)
                  for card in product(rank, suit))

full_deck_valued = {card: min(1 + rank.index(card[0]), 10)
                    for card in full_deck}


class Deck:

    def __init__(self):
        # self.suit = "CSHD"
        # self.rank = "A23456789TJQK"
        # self.full_deck = tuple(''.join(card) for card in product(self.rank, self.suit))
        # self.full_deck_valued = {card: min(1 + self.rank.index(card[0]), 10) for card in self.full_deck}
        # self.shuffled_deck = sample(self.full_deck, len(self.full_deck))
        self.shuffled_deck = sample(full_deck, len(full_deck))
        # self.hand = []
        # self.hand_valued = []

    # moved to hand
    # def initial_deal(self):
        # self.hand = [self.shuffled_deck.pop() for _ in range(2)]
        # return self.hand

    def deal_one_card(self):
        return self.shuffled_deck.pop()
        # new_card = self.shuffled_deck.pop()
        # self.hand.append(new_card)
        # return self.hand

    # def value_the_cards(self):
        # self.hand_valued = sum(self.full_deck_valued[card] for card in self.hand)
        # return self.hand_valued

#'''
# hep_test = Deck()
# hep_test.initial_deal()
# print(hep_test.hand)
# print(hep_test.deal_one_card())

#'''






