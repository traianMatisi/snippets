# Hangman - 100 days of python - day 7
# Author: Traian 15-6-24

from random import choice
#import os

play = True
words = ["zerozerozero", "oneoneone", "twotwotwo", "threethreethree", "fourfourfour", "fivefivefive", "sixsixsix", "sevensevenseven", "eighteighteight", "nineninenine", "tententen",]
word = choice(words).upper()
word = input("Type the secret word:\n==> ").upper().replace(" ", "")
letters = []
blanks = []
guesses = []
for i in word:
    letters.append(i)
for i in letters:
    blanks.append('_')
hanger = [
["_","_","_","_","_","_","_","_","_"," ",],
["|","/"," "," "," "," "," "," ","|"," ",],
["|"," "," "," "," "," "," "," ","O"," ",],
["|"," "," "," "," "," "," "," "," "," ",],
["|"," "," "," "," "," "," "," "," "," ",],
["|"," "," "," "," "," "," "," "," "," ",],
["|"," "," "," "," "," "," "," "," "," ",],
]
'''
Head [2][8]
Torso [3][8]
Arms [3][7] and [3][9]
Legs [4][7] and [4][9]
'''
while True:

    #os.system('clear')

    # prints the hanger
    for i in range(7):
        for j in range(10):
            print(hanger[i][j], end = ' ')
        print("")

    # prints the blanks line
    for blank in blanks:
        print(blank, end = " ")
    print("\n")

    # prints the made guesses
    for i in range(len(guesses)):
        print("Guesses --> ", guesses[i], sep = '-', end = " ")
    print("\n")

    # checking secret word and guessed word
    if blanks == letters:
        print("Congratulations, you won!\n")
        break
    elif hanger[4][9] == '\\':
        print("Sorry, you lost!\n")
        break

    # asks for a guess
    guess = input("Guess a letter:\n==> ").upper()
    guesses.append(guess)

    # sweeps the letters list
    if guess in letters:
        for i in range(len(letters)):
            if letters[i] == guess:
                blanks[i] = guess
    # loses 1 life
    else:
        if hanger[2][8] == 'O':
            hanger[2][8] = 'o'
        elif hanger[3][8] == ' ':
            hanger[3][8] = '|'
        elif hanger[3][7] == ' ':
            hanger[3][7] = '/'
        elif hanger[3][9] == ' ':
            hanger[3][9] = '\\'
        elif hanger[4][7] == ' ':
            hanger[4][7] = '/'
        elif hanger[4][9] == ' ':
            hanger[4][9] = '\\'
