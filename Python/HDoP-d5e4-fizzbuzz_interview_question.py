# Fizz buzz game (programming interview question) - 100 days of python - day 5
# Author: Traian 13-6-24

for i in range(1, 101):
    if i % 3 == 0 and  i % 5 == 0:
        print("Fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
