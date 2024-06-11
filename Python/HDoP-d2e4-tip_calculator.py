# Tip calculator
# Author: Traian 9-6-24

print("Welcome to Tip Calculator")
totalBill = float(input("What was the total bill? "))
totalPeople = int(input("How many people to plit the bill? "))
desiredPercentage = float(input("What percentage tip would you like to give? "))
individualBill = ((totalBill + (totalBill * (desiredPercentage/100)))/totalPeople)
print(f"Each person should pay: {round(individualBill, 2):.2f}")

