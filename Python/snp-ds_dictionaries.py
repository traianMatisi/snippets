# Keys can only be unique, never a iterable, anything else can be nested
"""
nested_dictionaries = {
    "dict_one": {
        "Boys":
            {"Miles": 12, "Feynman": 62},
        "Girls": {"Roxanne": 12, "Katia": 23},
    },
    "dict_two": {
        "Teachers": {"Math": "Traian"},
        "Student": "Problem",
    },
}
print(nested_dictionaries)
"""
original_dictionary = {"Luigi": 0, "Lucca": 7, "Leon": 8, "Lucas": 27, "Sandra": 36, "Traian": 38,}
#print(original_dictionary)
"""
print(original_dictionary.get("Traian"))

print(original_dictionary.keys())
print(original_dictionary.values())
print(original_dictionary.items())
for k, v in original_dictionary.items():
    print(k, v)

print(original_dictionary)
print(original_dictionary.pop("Lucas"))
"""
hand = {}
print(original_dictionary)
hand = dict(original_dictionary.popitem())
print(type(hand), hand)

print(original_dictionary)

"""

print(original_dictionary.get($KEY$)
print(original_dictionary.keys())
print(original_dictionary.values())
print(original_dictionary.items())
print(original_dictionary.pop($KEY$))
print(original_dictionary.popitem())
print(original_dictionary.update())
print(original_dictionary.copy())
print(original_dictionary.clear())
print(original_dictionary.fromkeys())
print(original_dictionary.setdefault())

"""

