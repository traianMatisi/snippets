# Password generator - 100 days of python - day 5
#
# ASCII uppercase letters: 65 to 90
# ASCII lowercase letters: 97 to 122
# ASCII numbers: 48 to 57
# ASCII symbols: 32 to 47, 58 to 64, 91 to 96, 122 to 126
# ASCII non printable: 0 to 31, and 127
#
# Author: Traian 13-6-24

from random import randint
from random import shuffle

#letters = int(input("How many letters do you want in your password: "))
#symbols = int(input("How many symbols do you want in your password: "))
#numbers = int(input("How many numbers do you want in your password: "))

password_while_string = ""
password_for_list = []
password_true = ""

letters = 4
numbers = 2
symbols = 2

counter = 0
while counter < letters:
    enter = randint(65, 122)
    if enter < 91 or enter > 96:
        password_while_string += chr(enter)
        counter += 1
counter = 0
while counter < symbols:
    enter = randint(32, 127)
    if enter < 48 or enter > 57 and enter < 65 or enter > 90 and enter < 97 or enter > 122:
        password_while_string += chr(enter)
        counter += 1
counter = 0
while counter < numbers:
    enter = randint(48, 58)
    password_while_string += chr(enter)
    counter += 1

for i in range(letters):
    x = randint(0, 1)
    if x == 0:
        password_for_list += chr(randint(65, 90))
    else:
        password_for_list += chr(randint(97, 122))
for i in range(symbols):
    x = randint(0, 3)
    if x == 0:
        password_for_list += chr(randint(32, 47))
    elif x == 1:
        password_for_list += chr(randint(58, 64))
    elif x == 1:
        password_for_list += chr(randint(91, 96))
    else:
        password_for_list += chr(randint(122, 126))
for i in range(numbers):
    password_for_list += chr(randint(48, 57))

password_size = 8
for i in range(0, password_size):
    password_true += chr(randint(32, 126))

print("While = ", password_while_string)
print("For = ", password_for_list)
print(password_true)

#shuffle(password_while_string)
shuffle(password_for_list)

print("While shuffled = TypeError: 'str' object does not support item assignment")
print("For shuffled = ", password_for_list)
