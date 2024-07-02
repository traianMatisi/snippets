# Blackjack - 100 days of python - day 10
# Author: Traian 28-6-24
# TODO: Use dictionaries instead of lists
# TODO: Attire to official cassino rules. Use 2 or more decks, split repeated cards, set bets, set bets proportions
# TODO: continue to modularize and shrink lines to less than 100
# TODO: Create display and clean terminal

import random
import os

def main():
    executing = True
    while executing:
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
        deck = ["Ace of spades", "2 of spades", "3 of spades", "4 of spades", "5 of spades", "6 of spades", "7 of spades", "8 of spades", "9 of spades", "10 of spades", "Jack of spades", "Queen of spades", "King of spades", "Ace of hearts", "2 of hearts", "3 of hearts", "4 of hearts", "5 of hearts", "6 of hearts", "7 of hearts", "8 of hearts", "9 of hearts", "10 of hearts", "Jack of hearts", "Queen of hearts", "King of hearts", "Ace of diamonds", "2 of diamonds", "3 of diamonds", "4 of diamonds", "5 of diamonds", "6 of diamonds", "7 of diamonds", "8 of diamonds", "9 of diamonds", "10 of diamonds", "Jack of diamonds", "Queen of diamonds", "King of diamonds", "Ace of clubs", "2 of clubs", "3 of clubs", "4 of clubs", "5 of clubs", "6 of clubs", "7 of clubs", "8 of clubs", "9 of clubs", "10 of clubs", "Jack of clubs", "Queen of clubs", "King of clubs",]
        random.shuffle(deck)

        player_hand = []
        dealer_hand = []
        for _ in range(2):
            player_hand.append(deck.pop())
            dealer_hand.append(deck.pop())
        player_total = sum_hand(player_hand)
        dealer_total = sum_hand(dealer_hand)

        first_hand(dealer_hand, player_hand)
        step()

        game_on = True
        while game_on:
            while True:
                first_hand(dealer_hand, player_hand)
                hit = input('Do you want to draw a card? [y/n] ').lower().strip()
                if hit == 'y':
                    player_hand.append(deck.pop())
                    player_total = sum_hand(player_hand)
                    print(f'You drew a {player_hand[-1]}')
                    if player_total > 21:
                        print(f'Player score: {player_total}, You bursted, the house wins!')
                        game_on = False
                        break
                elif hit == 'n':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    print('Yes or No answers, only')
                step()

            while game_on:
                second_hand(dealer_hand, player_hand)
                if dealer_total < 17:
                    dealer_hand.append(deck.pop())
                    dealer_total = sum_hand(dealer_hand)
                    print(f'Dealer drew a {dealer_hand[-1]}')
                    if dealer_total > 21:
                        print(f'House score: {dealer_total}, The house loses.\nCongratulations, you won!')
                        game_on = False
                        break
                    step()
                else:
                    break
            
            if game_on:
                if dealer_total > player_total:
                    print(f'The house wins!\nHouse: {dealer_total}\nPlayer: {player_total}')
                elif dealer_total < player_total:
                    print(f'Congratulations! You won!\nPlayer: {player_total}\nHouse: {dealer_total}')
                else:
                    print(f'Is a tie!\nPlayer: {player_total}\nHouse: {dealer_total}')
        
            answer = ''
            while True:
                answer = input('Do you wanna play another round? [y/n] ')
                if answer == 'y':
                    game_on = False
                    break
                elif answer == 'n':
                    game_on = False
                    executing = False
                    break
            os.system('cls' if os.name == 'nt' else 'clear')

    print('Thanks for playing Blackjack!')

def first_hand(dealer, player):
    print(f'Dealer hand: [\'{dealer[0]}\']')
    print(f'Player hand: {player}')

def second_hand(dealer, player):
    print(f'Player hand: {player}')
    print(f'Dealer hand: {dealer}')

def sum_hand(hand):
    value = 0
    for card in hand:
        if card[0] in '1JQK':
            value += 10
        elif card.startswith('A'):
            value += 11
        else:
            value += int(card[0])
    for card in hand:
        if value > 21 and card[0] == 'A':
            value -= 10
    return value

def step():
    input('Press ENTER to continue ')
    os.system('cls' if os.name == 'nt' else 'clear')

main()

'''
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from replit import clear
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)

  #Hint 5: Deal the user and computer 2 cards each using deal_card()
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

  while not is_game_over:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
'''