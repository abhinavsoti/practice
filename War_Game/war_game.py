import card_class
import deck_class
import player_class

player1 = player_class.Player('Abhinav')
player2 = player_class.Player('Saangvi')

print (f'Welcome {player1.name} & {player2.name} to the war game.')
print ('Let the game Begin!')

cnt = 1


for card in deck_class.new_deck.all_cards:
    if cnt == 1:
        player1.add_cards(card)
        cnt = 2
    elif cnt == 2:
        player2.add_cards(card)
        cnt = 1

print (player1)
print (player2)

loop_cnt = 1

while len(player1.all_cards) > 0 and len(player2.all_cards) > 0:
    player1_card = str(player1.all_cards[0])
    #print(player1_card)
    player1.all_cards.pop(0)
    player2_card = str(player1.all_cards[0])
    #print(player2_card)
    player2.all_cards.pop(0)
    
    # check rank of both cards and compare them
    player1_rank = card_class.values[player1_card.split(' ')[0]]
    #print(player1_rank)
    player2_rank = card_class.values[player2_card.split(' ')[0]]
    #print(player2_rank)

    if player1_rank > player2_rank:
        player1.add_cards(player1_card)
        player1.add_cards(player2_card)
    elif player1_rank < player2_rank:
        player2.add_cards(player2_card)
        player2.add_cards(player1_card)
    elif (player1_rank == player2_rank) and (len(player1.all_cards) == 1 or len(player1.all_cards) == 0):
        player2.add_cards(player2_card)
        player2.add_cards(player1_card)
    elif (player1_rank == player2_rank) and (len(player2.all_cards) == 1 or len(player2.all_cards) == 0):
        player1.add_cards(player1_card)
        player1.add_cards(player2_card)
    elif (player1_rank == player2_rank) and len(player1.all_cards) == 2:
        pass
    elif (player1_rank == player2_rank) and len(player2.all_cards) == 2:
        pass
    elif (player1_rank == player2_rank) and len(player1.all_cards) > 2 and len(player2.all_cards) > 2:
        player1_card_1, player1_card_2, player1_card_3 = str(player1.all_cards[0]),str(player1.all_cards[1]),str(player1.all_cards[2])
        player2_card_1, player2_card_2, player2_card_3 = str(player2.all_cards[0]), str(player2.all_cards[1]), str(player2.all_cards[2])

        player1.all_cards.pop(0)
        player1.all_cards.pop(0)
        player1.all_cards.pop(0)
        player2.all_cards.pop(0)
        player2.all_cards.pop(0)
        player2.all_cards.pop(0)

        if (card_class.values[player1_card_1.split(' ')[0]] > card_class.values[player2_card_1.split(' ')[0]]) \
                or (card_class.values[player1_card_2.split(' ')[0]] > card_class.values[player2_card_2.split(' ')[0]]) \
                or (card_class.values[player1_card_3.split(' ')[0]] > card_class.values[player2_card_3.split(' ')[0]]):

            add_cards = [player1_card, player2_card,player1_card_1, player1_card_2, player1_card_3, player2_card_1, player2_card_2, player2_card_3]
            player1.add_cards(add_cards)

        elif (card_class.values[player1_card_1.split(' ')[0]] < card_class.values[player2_card_1.split(' ')[0]]) \
                or (card_class.values[player1_card_2.split(' ')[0]] < card_class.values[player2_card_2.split(' ')[0]]) \
                or (card_class.values[player1_card_3.split(' ')[0]] < card_class.values[player2_card_3.split(' ')[0]]):

            add_cards = [player1_card, player2_card, player2_card_1, player2_card_2, player2_card_3, player1_card_1, player1_card_2, player1_card_3]
            player2.add_cards(add_cards)


    print ('Check the length again for player 1 and player 2')
    print (len(player1.all_cards))
    print (len(player2.all_cards))

    if loop_cnt == 1000:
        break

    loop_cnt += 1

# Check which player has all the cards and declare him/her the winner of the game

if len(player1.all_cards) == 0:
    print(f'Congratulations {player2.name} is the winner of this game')
elif len(player2.all_cards) == 0:
    print(f'Congratulations {player1.name} is the winner of this game')
else:
    print ('The game is a tie! Please play again')