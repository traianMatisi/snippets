# 100 days of python - day 9
# Author: Angela Yu 28-10-20

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)

#🚨 Do not change the code below ##Sorry, Angela, I chenged a bit
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
for i in range(len(travel_log)):
    print(travel_log[i])