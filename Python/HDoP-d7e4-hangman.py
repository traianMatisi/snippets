# Hangman - 100 days of python - day 7
# Author: Traian 15-6-24

from time import sleep
from random import choice
import os
from hangman_resources import word_list
from hangman_resources import hanger
from hangman_resources import logo

game = True
while game:
    print(logo)
    sleep(1.7)

    word = choice(word_list).lower()
    display = []
    guesses = []
    for blank in word:
        display.append("_")
    lives = 6

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(hanger[lives])
        print("Secret word ", " ".join(display))
        print("Guesses made => ", " ".join(guesses))

        if '_' not in display:
            print("Congratulations, you won!")
            sleep(3)
            break
        elif lives == 0:
            print(f"Sorry, you lost!\nThe word was {word}")
            sleep(5)
            break

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Sorry, only single characters allowed")
            sleep(3)
            continue
        elif guess in guesses:
            print("You already tried the letter")
            sleep(3)
            continue
        elif ord(guess) < 97 or ord(guess) > 122:
            print("Sorry, invalid input\nOnly letters and without signals")
            sleep(3)
            continue
        else:
            guesses.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            lives -= 1

    answer = False
    while not answer:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        answer = input("Do you wanna play again? [Y/N] ").lower()
        if answer == 'y':
            print("Yay, let\'s roll!")
            break
        elif answer == 'n':
            print("Hope we could play again, soon.")
            sleep(1.7)
            game = False
        else:
            print("Sorry, I didn\'t understand you.\nY or N, yes or no answers only")
            sleep(1.7)
            answer = False
        os.system('cls' if os.name == 'nt' else 'clear')
