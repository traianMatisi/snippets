import os
from time import sleep
# calculator opening
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)
sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')

# __MAIN__ #
def main():
    # Variables declaration
    equat = ['_','_','_','=','_']
    opert = { 
        # Keys are compared to operation input
        # Values are the defined functions
        # I didn't knew python could be used like this
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }
    on = True
    ans = 0
    again = ''
    while on:
        make_equation(equat)
        # First input or previous answer
        if again == 'Y':
            equat[0] = ans
        else:
            equat[0] = float(input('Input FIRST NUMBER:\n-=> '))
        again = ''
        # Input basic math operation + - * /
        make_equation(equat)
        equat[1] = str(input('Input OPERATION:\n-=> '))
        # Second input
        make_equation(equat)
        equat[2] = float(input('Input SECOND NUMBER:\n-=> '))
        # Operation
        make_math = opert[equat[1]]
        equat[-1] = make_math(equat[0], equat[2])
        # Answer memorization
        ans = equat[-1]
        # Result output
        make_equation(equat)
        # Memory cleansing
        for i in range(-1,3):
            equat[i] = '_'
        # Continue?
        while True:
            print('Type \'y\' to continue calculating with this answer')
            print('Othewise, type \'n\' to CE clear everything')
            again = input('Type \'off\' to quit CALC:\n[yes/no/off] -=> ').upper()
            if again.startswith('Y') or again.startswith('N'):
                break
            elif again == 'OFF':
                print('Thanks for using CALC\nByBye!')
                sleep(3)
                on = False
                break

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

def make_equation(terms):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Current equation: ')
    for term in terms:
        print(term, end = ' ')
    print('\n')

main()
