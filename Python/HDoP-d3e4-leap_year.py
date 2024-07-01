# Leap year calculation
#
# To calculate leap years:
#   The year must be divisible by 4
#   The year must not be divisible by 100, unless it is divisible by 400
#
# Leap years were created in 45 bce, and fixed in 1582, will need fixing again soon
# https://time.com/4237292/leap-year-leap-day-history/
#
# Here are some explanation for the reason for leap years existence
# https://www.youtube.com/watch?v=xX96xng7sAE
#
# Author: Traian 10-6-24

year = int(input("Type any year: "))

print("Block if/elif/else")

if year % 4 != 0:
    print(f"{year} is not a leap year")

elif year % 100 != 0:
    print(f"{year} is a leap year")

elif year % 400 != 0:
    print(f"{year} is not a leap year")

else:
    print(f"{year} is a leap year")

print("Block if ... and ...")

if year % 4 != 0:
    print(f"{year} is not a leap year")

elif year % 100 == 0 and year % 400 != 0:
    print(f"{year} is not a leap year")

else:
    print(f"{year} is a leap year")

# TODO: print("Block nested")
# A good exercise is to make this snippet with nested if/else

# old solution - 2021
# anoInput = float(input('Digite um ano qualquer: '))
# biss1 = int(anoInput % 4)
# biss2 = int(anoInput % 400)
# biss3 = int(anoInput % 100)
# print('É ano bissexto.') if biss1 == 0 and biss3 != 0 or biss2 == 0 else print('Não é ano bissexto')
