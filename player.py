# receives cards
# calculates value of cards
# assesses whether to hit or stay

# collaborates with Dealer, Cards, Hand

class Player:

    def __init__(self):
        self.hand = 0

    def get_card(self):
        # needs to be a random selection of remaining cards in the deck
        self.hand += 2  # randomly select from a deck
'''
hep_player = Player()
joe_dealer = Player()



while hep_player.hand <= 21:
    hit = input("Another card? Y/n").lower()
    if hit == 'y':
        hep_player.get_card()
    else:
        break

while joe_dealer.hand < 17:
    joe_dealer.get_card()


print("Hope's hand: ", hep_player.hand)
print("Dealer's hand: ", joe_dealer.hand)
'''




