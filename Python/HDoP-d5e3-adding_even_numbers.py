# Highest score - 100 days of python - day 5
# Author: Traian 13-6-24

sum_with_stepping = 0
sum_with_module = 0

for i in range(0,101, 2):
    sum_with_stepping += i

for i in range(0, 101):
    if i % 2 == 0:
        sum_with_module += i

print(sum_with_stepping)
print(sum_with_module)
