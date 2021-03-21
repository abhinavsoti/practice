import card_class
import deck_class

class Player:
    '''
    Player Class: This class is defined to accomplish 3 things
    1. Take users name as input
    2. Provide functions like removing and adding cards to the players list
    3. Returing how many cards does the player have.
    '''

    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type (self.all_cards):
            # Add mutliple cards to the list
            self.all_cards.extend(new_cards)
            print('called extend method')
        else:
            # Add single card to the list
            self.all_cards.append(new_cards)
            #print ('called append method')

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


#new_player = Player('Abhinav')
#print (deck_class.mycard)
#new_player.add_cards(deck_class.mycard)
#print (new_player)