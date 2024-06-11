# Body Mass Index 1.0
# Author: Traian 9-6-24

height = float(input("Please, type your height in meters: "))
weight = float(input("Please type your weight in kilograms: "))

bmi = int(weight / height ** 2)

print(f"Your BMI is {bmi}")

