# Rollercoaster auth
# Author: Traian 10-6-24

print("Welcome to the rollercoaster!")
height = float(input("Please, type your height in meters: "))
age = int(input("Please, input your age: "))
bill = 0

if height > 1.20:
    
    if age > 18:
        print("Your toll is $12")
        bill = 12

    elif age >= 12:
        print("Your tol is $7")
        bill = 7

    else:
        print("Your toll is $5.")
        bill = 5

    answer = input("Do you want to take a photo for extra $3? [Y/N] ")
    if answer == 'y' or answer == 'Y':
        bill += 3
    
    print(f"Your total bill is {bill}")
    print("Enjoy the ride!")

else:
    print("Sorry, for security reasons you have to be at least 1.20m tall.")
