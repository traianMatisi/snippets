print("Hello, friend...")

import random
import os
import time

def main():
    print_logo()

    deck = set_deck()
    random.shuffle(deck)

    player_hand = []
    dealer_hand = []
    game_on = True

    for _ in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())  

    player_total = sum_hand(player_hand)
    dealer_total = sum_hand(dealer_hand)

    print('## SCORE ##')
    print(f'Dealer hand: {dealer_hand[0]}, ONE CONCEALED CARD ==> Total house: {sum_hand(dealer_hand[0])}')
    print(f'Player hand: {player_hand}\nTotal player: {sum([player_hand])}\n')
    
    os.system('cls' if os.name == 'nt' else 'clear')

    while dealer_game and player_game:
        while True:
            hit = input('Do you want to draw a card? [y/n] ').lower().strip()
            if hit == 'y':
                player_hand.append(deck.pop())
                player_total = sum_hand(player_hand)
                print(f'You drew a {player_hand[-1]}')
                if player_total > 21:
                    print(f'Player score: {player_total}, You bursted, the house wins!')
                    player_game = False
                time.sleep(3.5)
                break
            elif hit == 'n':
                #os.system('cls' if os.name == 'nt' else 'clear')
                player_game = False
                break
            else:
                print('Yes or No answers, only')
        
        if dealer_total < 17:
            dealer_hand.append(deck.pop())
            dealer_total = sum_hand(dealer_hand)
            print(f'Dealer drew a {dealer_hand[-1]}')
            if dealer_total > 21:
                print(f'House score: {dealer_total}, The house loses.\nCongratulations, you won!')
                dealer_game = False
            time.sleep(3.5)
        else:
            print(f'{dealer_hand}\nHouse stands in {dealer_total}')
            time.sleep(3.5)

        player_total = sum_hand(player_hand)
        dealer_total = sum_hand(dealer_hand)

        print('CURRENT SCORE')
        print(f'Dealer hand: {dealer_hand}\nTotal dealer: {dealer_total}')
        print(f'Player hand: {player_hand}\nTotal player: {player_total}')

        time.sleep(3.5)

        #os.system('cls' if os.name == 'nt' else 'clear')

    if not (player_game and dealer_game):
        if dealer_total == player_total:
            print('Is a tie!\nPlayer: {player_total}\nHouse: {dealer_total}')
        elif dealer_hand == 21:
            print('Blackjack! The house wins!')
        elif player_hand == 21:
            print('Blackjack! You win\nCongratulations')
        elif dealer_hand > player_hand:
            print(f'The house wins!\nHouse: {dealer_total}\nPlayer: {player_total}')
        elif dealer_hand < player_hand:
            print(f'Congratulations! You won!\nPlayer: {player_total}\nHouse: {dealer_total}')

    print('Thanks for playing Blackjack!')

def print_logo():
    print("""
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """)
    time.sleep(4)

def set_deck():
    return ["Ace of spades", "2 of spades", "3 of spades", "4 of spades", "5 of spades", "6 of spades", "7 of spades", "8 of spades", "9 of spades", "10 of spades", "Jack of spades", "Queen of spades", "King of spades", "Ace of hearts", "2 of hearts", "3 of hearts", "4 of hearts", "5 of hearts", "6 of hearts", "7 of hearts", "8 of hearts", "9 of hearts", "10 of hearts", "Jack of hearts", "Queen of hearts", "King of hearts", "Ace of diamonds", "2 of diamonds", "3 of diamonds", "4 of diamonds", "5 of diamonds", "6 of diamonds", "7 of diamonds", "8 of diamonds", "9 of diamonds", "10 of diamonds", "Jack of diamonds", "Queen of diamonds", "King of diamonds", "Ace of clubs", "2 of clubs", "3 of clubs", "4 of clubs", "5 of clubs", "6 of clubs", "7 of clubs", "8 of clubs", "9 of clubs", "10 of clubs", "Jack of clubs", "Queen of clubs", "King of clubs",]

def sum_hand(hand):
    value = 0
    for card in hand:
        if card.startswith('J') or card.startswith('Q') or card.startswith('K') or card.startswith('1'):
            value += 10
        elif card.startswith('A'):
            value += 11
        else:
            value += int(card[0])
    for card in hand:
        if value > 21 and card.startswith('A'):
            value -= 10
    return value

main()

