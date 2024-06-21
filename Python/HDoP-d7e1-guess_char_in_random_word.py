# Random word - 100 days of python - day 7
# Author: Traian 19-6-24

from random import choice

words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",]

word = choice(words).lower()

guess = input("Guess a letter: ").lower()

for i in word:
    if i == guess:
        print(f"The {i} letter was guessed right")
        break
    else:
        print("Guess is not in the word")
