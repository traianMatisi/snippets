# Checking winner - 100 days of python - day 7
# Author: Traian 19-6-24

from random import choice
import os

words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",]
hanger = [
"""
+------+
|      |
|      0
|     /|\\
|     / \\
|
==========
""",
"""
+------+
|      |
|      O
|     /|\\
|     /
|
==========
""",
"""
+------+
|      |
|      o
|     /|\\
|
|
==========
""",
"""
+------+
|      |
|      O
|     /|
|
|
==========
""",
"""
+------+
|      |
|      o
|      |
|
|
==========
""",
"""
+------+
|      |
|      O
|
|
|
==========
""",
"""
+------+
|      |
|      °
|
|
|
==========
""",
]
word = choice(words).lower()
word = "liquidificador"
display = []
guesses = []
for blank in word:
    display.append("_")
lives = 5

while True:
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(hanger[lives])
    print("Secret word ", " ".join(display))
    print("Guesses made => ", " ".join(guesses))

    if '_' not in display:
        print("Congratulations, you won!")
        break
    elif lives == 0:
        print("Sorry, you lost!")
        break

    guess = input("Guess a letter: ").lower()
    guesses.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
