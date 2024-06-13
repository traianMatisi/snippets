# Bill russian roullette
# Author: Traian 11-6-24

from random import randint

input_string = input("Type your friends' names separated by commas: ").replace(" ", "")

friends = input_string.split(",")

#print(f"{friends[randint(0, len(friends)-1)]} will pay the bill today")

victim_index = randint(0, len(friends)-1)
victim = friends[victim_index]

print(f"{victim} will pay the bill today")
