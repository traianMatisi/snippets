# Highest score - 100 days of python - day 5
# Author: Traian 13-6-24

scores = [78.0, 65.0, 89.0, 86.0, 55.0, 91.0, 64.0, 89.0,]
high_score = 0

for score in scores:
    if high_score < score:
        high_score = score

print(f"The highest score in the class is: {high_score}")
