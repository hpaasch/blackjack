# defines possible cards to play
# shuffles
# delivers cards

from itertools import product
from random import sample

suit = "CSHD"
rank = "A23456789TJQK"

full_deck = tuple(''.join(card)
                  for card in product(rank, suit))

full_deck_valued = {card: min(1 + rank.index(card[0]), 10)
                    for card in full_deck}


class Deck:

    def __init__(self):
        self.shuffled_deck = sample(full_deck, len(full_deck))

    def deal_one_card(self):
        return self.shuffled_deck.pop()
