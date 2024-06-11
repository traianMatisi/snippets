# Pizza app selector
# Author: Traian 10-6-24

pizzaSize = input("Pizza size [S/M/L]")
pepperoni = input("Pepperoni [Y/N]")
extraCheese = input("Extra cheese [Y/N]")
bill = 0

if pizzaSize == 'S':
    bill += 15
elif pizzaSize == 'M':
    bill += 20
else:
    bill += 25

if pepperoni == 'Y':
    if pizzaSize == 'S':
        bill += 2
    else:
        bill += 3

if extraCheese == 'Y':
    bill += 1

print(f"Total bill: ${bill}")
