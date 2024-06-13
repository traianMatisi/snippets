# Random integer and rndom float - 100 days of python day 4
# Author: Traian 11-6-24

from random import randint
from random import random

random_integer = randint(0, 100)

random_float = random()

print(f"Random integer = {random_integer}")
print(f"Random float = {random_float}")
print(f"Random float bigger than 1 = {random_float * 10}")
