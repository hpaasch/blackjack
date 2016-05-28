# defines possible cards to play
# shuffles
# delivers cards

from itertools import product
from random import sample, choice


class Deck:

    def __init__(self):
        self.suit = "CSHD"
        self.rank = "A23456789TJQK"
        self.full_deck = tuple(''.join(card) for card in product(self.rank, self.suit))
        self.full_deck_valued = {card: min(1 + self.rank.index(card[0]), 10) for card in self.full_deck}
        self.shuffled_deck = sample(self.full_deck, len(self.full_deck))
        self.hand = []
        self.hand_valued = []
        # print(self.full_deck)
        # print(self.full_deck_valued)
        # print(self.shuffled_deck)

    def initial_deal(self):
        self.hand = [self.shuffled_deck.pop() for _ in range(2)]
        return self.hand

    def value_the_cards(self):
        self.hand_valued = sum(self.full_deck_valued[card] for card in self.hand)
        # hephep = 8
        return self.hand_valued  # hephep

    def deal_one_card(self):
        new_card = self.shuffled_deck.pop()
        self.hand.append(new_card)
        return self.hand


# hep_test = Deck()
# hep_test.initial_deal()
# hep_test.deal_one_card()
# hep_test.deal_one_card()
# hep_test.deal_one_card()

# print(hep_test.value_the_cards())
# print(hep_test.deal_one_card())
# hep_test.value_the_cards()
# print(hep_test.hand)
# print(hep_test.value_the_cards())
# print(hep_test.hand_valued)



