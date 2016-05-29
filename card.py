# holds values
# holds suits

# collaborates with the deck

from itertools import product


class Card:

    suit = "CSHD"
    rank = "A23456789TJQK"

    full_deck = tuple(''.join(card)
                      for card in product(rank, suit))

    full_deck_valued = {card: min(1 + rank.index(card[0]), 10)
                        for card in full_deck}