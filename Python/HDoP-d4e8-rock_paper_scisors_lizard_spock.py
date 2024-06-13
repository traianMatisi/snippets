# Rock paper scissors lizard Spock - 100 days of python - day 4
#Author: Traian 12-6-24

from random import randint

def lizard():
  print("""
                        )/_
              _.--..---"-,--c_
          \L..'           ._O__)_
  ,-.     _.+  _  \..--( /
    `\.-''__.-' \ (     \_
      `'''       `\__   /\\
                  ')
  """)

def rock():
  print("""
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """)

def paper():
  print("""
      _______
  ---'   ____)____
            ______)
            _______)
          _______)
  ---.__________)
  """)

def scissors():
  print("""
      _______
  ---'   ____)____
            ______)
        __________)
        (____)
  ---.__(___)
  """)

def spock():
  print("""
    _     _ _
  /\ \   / / |
  \ \ \ / / /
  /\        |
  \         |
   \_______/
    |_____|
  """)

print("ROCK, PAPER, scissors, LIZARD, SPOCK!")
choices = [-1, -1]
choices[0] = randint(0, 4)
choices[1] = int(input("""
Escolha sua jogada:
      Pedra   [0]
      Papel   [1]
      Tesoura [2]
      Lagarto [3]
      Spock   [4]
      ==> """))
#choices[1] = int(input("==> "))

for i in choices:
  if i == 0:
    rock()
  elif i == 1:
    paper()
  elif i == 2:
    scissors()
  elif i == 3:
    lizard()
  elif i == 4:
    spock()

if choices[0] == choices[1]:
  print("DRAW! Let\'s play again!")
elif choices[0] == 0 and choices[1] == 1 or choices[0] == 1 and choices[1] == 0:
  print("Paper covers Rock!")
elif choices[0] == 0 and choices[1] == 2 or choices[0] == 2 and choices[1] == 0:
  print("Rock crushes scissors!")
elif choices[0] == 0 and choices[1] == 3 or choices[0] == 3 and choices[1] == 0:
  print("Rock crushes Lizard!")
elif choices[0] == 0 and choices[1] == 4 or choices[0] == 4 and choices[1] == 0:
  print("Spock vaporizes Rock!")
elif choices[0] == 1 and choices[1] == 2 or choices[0] == 2 and choices[1] == 1:
  print("Scissors cuts Paper!")
elif choices[0] == 1 and choices[1] == 3 or choices[0] == 3 and choices[1] == 1:
  print("Lizard eats Paper!")
elif choices[0] == 1 and choices[1] == 4 or choices[0] == 4 and choices[1] == 1:
  print("Paper disproves Spock!")
elif choices[0] == 2 and choices[1] == 3 or choices[0] == 3 and choices[1] == 2:
  print("Scissors decapitates Lizard!")
elif choices[0] == 2 and choices[1] == 4 or choices[0] == 4 and choices[1] == 2:
  print("Spock smashes Scissors!")
elif choices[0] == 3 and choices[1] == 4 or choices[0] == 4 and choices[1] == 3:
  print("Lizard poisons Spock!")
else:
  print("Invalid option, please try to play again")
