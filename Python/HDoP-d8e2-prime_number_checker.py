# Prime numbers checker - 100 days of python - day 8
# Author: Traian 20-6-24

def main():
    number = int(input("Type any whole number: "))
    prime_checker_a(number)
    #prime_checker_b(number)
    #prime_checker_c(number)

def prime_checker_a(number):
    if number >= -1 and number <= 1:
        print(f"3rd check: {number} is not prime by definition.")
    elif number >= -3 and number <= 3:
        print(f"3rd check: {number} is prime.")
    else:
        for i in range(abs(number) * - 1 + 1, abs(number)):
            if i >= -1 and i <= 1:
                continue
            elif number % i == 0:
                print(f"3rd check: {number} is not prime")
                break
            elif i == abs(number) - 1:
                print(f"3rd check: {number} is prime")

def prime_checker_b(number):
    counter = 0
    for i in range(abs(number) * - 1, abs(number) + 1):
        if i == 0:
            continue
        elif number % i == 0:
            counter += 1
    if counter == 4:
        print(f"2nd check: {number} is prime")
    else:
        print(f"2nd check: {number} is not prime")

def prime_checker_c(number):
    counter = 0
    if number >= 0:
        for i in range(1, number+1):
            if number % i == 0:
                counter += 1
        if counter == 2:
            print(f"1st check: {number} is prime")
        else:
            print(f"1st check: {number} is not prime")
    else:
        for i in range(number, 0):
            if number % i == 0:
                counter += 1
        if counter == 2:
            print(f"1st check: {number} is prime")
        else:
            print(f"1st check: {number} is not prime")

main()
