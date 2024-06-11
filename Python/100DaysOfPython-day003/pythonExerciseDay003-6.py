# Love calculator
# Based on the buzzfeed article
# https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love
#
# Author: Traian 11-6-24

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = (name1 + name2).lower()

t = name1.count("t")
r = name1.count("r")
u = name1.count("u")
e = name1.count("e")
l = name1.count("l")
o = name1.count("o")
v = name1.count("v")
e = name1.count("e")

score = ((t + r + u + e) * 10) + l + o + v + e

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like Coke and Menthos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
