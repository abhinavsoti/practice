import card_class
import random

class deck:

    def __init__(self):
        self.all_cards = []

        for suit in card_class.suits:
            for rank in card_class.ranks:
                # Create the card object
                created_card = card_class.card(suit,rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

 #   def deal_one(self):
 #       return self.all_cards.pop()



print("Preparing the new deck now")
new_deck = deck()
#print(new_deck.all_cards[0])
new_deck.shuffle()
#mycard = new_deck.all_cards[0]
#my_card_rank = new_deck.all_cards
#print(mycard)