original_dictionary = {"Traian": 38, "Sandra": 36, "Lucas": 27}
print(original_dictionary)
for k, v in original_dictionary.items():
    print(k, v)

# Keys can only be unique, never a iterable, anything else can be nested
nested_dictionary = {"one":{"Boy": "Miles", "Girl": "Roxanne",}, "two":{"Teacher": "Math", "Student": "Problem",},}
print(nested_dictionary)

