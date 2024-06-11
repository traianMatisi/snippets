# Body Mass Index 2.0
# Author: Traian 10-6-24
# TODO: reorder the elif to avoid warning ideal weight to normal weight people

height = float(input("Please, type your height in meters: "))
weight = float(input("Please type your weight in kilograms: "))

bmi = round(weight / height ** 2)

print(f"Your BMI is {bmi}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obese")
else:
    print("Clinically obese")

ideal = 21.5 * height ** 2
upLimit = 24 * height ** 2
lowLimit = 18.5 * height ** 2
print(f"Your ideal weight is: {ideal:.2f}")
print(f"Your upper limit weight is: {upLimit:.2f}")
print(f"Your lower limit weight is: {lowLimit:.2f}")

print("This mock analisis don't take in consideration the difference between fat and muscle.")
