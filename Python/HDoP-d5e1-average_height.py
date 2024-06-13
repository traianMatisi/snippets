# Average height - 100 days of python - day 5
# Author: Traian 13-6-24


people_heights = input("Input some comma separated people\'s height: ").replace(" ", "").split(",")
total_height = 0
list_len = 0

for i in people_heights:
    total_height += float(i)
    list_len += 1

average_height = total_height / list_len

print(f"{average_height:.6f}")
