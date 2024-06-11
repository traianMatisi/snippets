# Rollercoaster auth
# Author: Traian 10-6-24

print("Welcome to the rollercoaster!")
height = float(input("Please, type your height in meters: "))
age = int(input("Please, input your age: "))

if height > 1.20:
    if age > 18:
        print("Your toll is $12")
    elif age >= 12:
        print("Your tol is $7")
    else:
        print("Your toll is $5.")
    print("Enjoy the ride!")
else:
    print("Sorry, for security reasons you have to be at least 1.20m tall.")
