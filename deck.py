# defines possible cards to play
# shuffles
# delivers cards

# collaborates with hand, dealer, player

# create deck as tuples? then can add values more easily. not as strings.
# can put "used" tuple in a list and check to see if something used. not so efficient.
# can pop tuple from the list as it is dealt. more efficient, but need to read up on pop

from itertools import product
from random import sample, choice


# class Deck:

def deal_one(): # __init__():
    suit = "CSHD"
    rank = "A23456789TJQK"
    fake_card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    dealt_card = choice(fake_card_values)
    full_deck = tuple(''.join(card) for card in product(rank, suit))
    full_deck_valued = {card: min(1 + rank.index(card[0]), 10) for card in full_deck}
    shuffled_deck = sample(full_deck, len(full_deck))
    print(full_deck)
    print(full_deck_valued)
    print(shuffled_deck)
    print(dealt_card)
    return dealt_card
# dealt_card could return the value in the tuple.



