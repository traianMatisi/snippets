from random import choice

words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",]

word = choice(words).lower()
word = "liquidificador"
letters = []
for letter in word:
    letters.append(letter)
display = []
for blank in letters:
    display.append("_")

guess = input("Guess a letter: ").lower()

if guess in letters:
    for i in range(len(letters)):
        if letters[i] == guess:
            display[i] = guess

for i in range(len(letters)):
    if letters[i] == guess:
        print(f"The {guess} letter was guessed right")
        display[i] = guess
    else:
        print("Guess is not in the word")

for i in range(len(display)):
    print(display[i], end = "")

