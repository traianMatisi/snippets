# Paint cans calculator - 100 days 0f python
# Author: traian 20-6-24

from math import ceil

def main():
    paint_efficiency = 5 # each can covers 5m^2

    height = int(input("Type the height of the wall you're painting? "))
    width = int(input("Now, type the wall's width: "))
    answer = int(ceil(calculator(height = height, paint_efficiency = paint_efficiency, width = width)))

    print(f"We'll need {answer} cans of paint to cover the wall.")

def calculator(width, height, paint_efficiency):
    return (width * height)/paint_efficiency

main()
