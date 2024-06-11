# Lifetime left
# Author: Traian 9-6-24
# TODO Improve using datetime import functions and count leap years

# 90 * 365 = 32850
# 90 * 52 = 4680
# 90 * 12 = 1080

print("Lifetime left")

age = int(input("Please, type your current age:" ))

yearsLeft = 90 - age
daysLeft = yearsLeft * 365
weeksLeft = yearsLeft * 52
monthsLeft = yearsLeft * 12
print(f"You still have {daysLeft} days, or {weeksLeft} weeks, or {monthsLeft} months, or {yearsLeft} years")

