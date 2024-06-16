# Hangman - 100 days of python - day 7
# Author: Traian 15-6-24

from random import choice
import os

play = True
words = ["zerozerozero", "oneoneone", "twotwotwo", "threethreethree", "fourfourfour", "fivefivefive", "sixsixsix", "sevensevenseven", "eighteighteight", "nineninenine", "tententen",]
word = choice(words).upper()
letters = []
for i in word:
    letters.append(i)
blank = []
for i in letters:
    blank.append('_')
hanger = [
["_","_","_","_","_","_","_","_","_"," ",],
["|","/"," "," "," "," "," "," ","|"," ",],
["|"," "," "," "," "," "," "," ","O"," ",],
["|"," "," "," "," "," "," "," "," "," ",],
["|"," "," "," "," "," "," "," "," "," ",],
["|"," "," "," "," "," "," "," "," "," ",],
["|"," "," "," "," "," "," "," "," "," ",],
]

# Head [2][8]
# Torso [3][8]
# Arms [3][7] and [3][9]
# Legs [4][7] and [4][9]

while play == True:

    #os.system('clear')

    for i in range(7):
        for j in range(10):
            print(hanger[i][j], end = ' ')
        print("")

    for i in range(len(blank)):
        print(blank[i], end = " ")
    print("\n")

    guess = input("Guess a letter:\n==> ").upper()

    for i in range(len(letters)):
        if blank == letters:
            print("Congratulations, you won!")
            play = False
        elif letters[i] == guess:
            blank[i] = guess
        elif hanger[2][8] == 'O':
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
            print("Sorry, you lost")
