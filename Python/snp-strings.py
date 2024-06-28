the_string = "Big-ass \"imutable\" string"

print(the_string)

the_string = the_string.replace('i', '@')

print(the_string)

""" 
my_string = "Traian Matisi de Lima Vaz"
first_name = "Traian"
last_name = "Matisi"

print("Slice [5:15:2] => ", my_string[5:15:2])
print("str_a + str_b, sep='@', end='#' => ", first_name, last_name, sep = '@', end = '#')
print("len(my_string) = ", len(my_string))
print(".swapcase()", my_string.swapcase())
print(".casefold()", my_string.casefold())
print(".upper()", my_string.upper())
print(".lower()", my_string.lower())
print(".capitalize()", my_string.capitalize())
print(".title()", my_string.title())
print(".encode()", my_string.encode())
print("", my_string.count('a'))
print("", my_string.find('ian')) # also L and R
print("", my_string.index('ian')) # also L and R
print("", my_string.strip()) # also L and R
print("", my_string.replace('ian', 'yain'))
print("", my_string.replace('a', ' '))
print("", my_string.split(" ")) # also L and R
print("", my_string.join("~"))

class str(object='')
class str(object=b'', encoding='utf-8', errors='strict')
    >>>str(b'Zoot!')
    "b'Zoot!'"
str.capitalize()
str.casefold()
str.center(width[, fillchar])
str.count(substr[, start[, end]])
str.encode(encoding='utf-8', errors='strict')
str.endswith(suffix[, start[, end]])
str.expandtabs(tabsize=8)
str.find(substr[, start[, end]])
str.format(*args, **kwargs)
    "The sum of 1 + 2 is {0}, not {1}".format(1+2, 2+2)
str.format_map(mapping)
str.index(substr[, start[, end]])
str.isalnum()
str.isalpha()
str.isascii()
str.isdecimal()
str.isdigit()
str.isidentifier()
str.iskeyword()
str.islower()
str.isnumeric()
str.isprintable()
str.isspace()
str.isupper()
str.join(iterable)
str.ljust(width[, fillchar])
str.lower()
str.lstrip([chars])
    >>>'   spacious   '.lstrip()
    'spacious   '
    >>>'www.example.com'.lstrip('cmowz.')
    'example.com'
static str.maketrans(x[, y[, z]])
str.partition(sep)
str.removeprefix(prefix, /)
str.removesuffix(suffix, /)
str.replace(old, new[, count])
str.rfind(sub[, start[, end]])
str.rindex(sub[, start[, end]])
str.rjust(width[, fillchar])
str.rpartition(sep)
str.rsplit(sep=None, maxsplit=-1)
str.rstrip([chars])
str.split(sep=None, maxsplit=-1)
str.splitlines(keepends=False)
str.startswith(prefix[, start[, end]])
str.strip([chars])
str.swapcase()
str.title()
str.translate(table)
str.upper()
str.zfill(width)

0. The quick brown fox jumps over the lazy dog. (35 letters)

1. Waltz, bad nymph, for quick jigs vex. (28 letters)

2. Quick zephyrs blow, vexing daft Jim. (29 letters)

3. Sphinx of black quartz, judge my vow. (29 letters)

4. Two driven jocks help fax my big quiz. (30 letters)

5. Five quacking zephyrs jolt my wax bed. (31 letters)

6. The five boxing wizards jump quickly. (31 letters)

7. Pack my box with five dozen liquor jugs. (32 letters)

8. The quick brown fox jumps over the lazy dog. (35 letters)

9. Jinxed wizards pluck ivy from the big quilt. (36 letters)

10. Crazy Fredrick bought many very exquisite opal jewels. (46 letters)

11. We promptly judged antique ivory buckles for the next prize. (50 letters)

12. A mad boxer shot a quick, gloved jab to the jaw of his dizzy opponent. (54 letters)

13. Jaded zombies acted quaintly but kept driving their oxen forward. (55 letters)

14. The job requires extra pluck and zeal from every young wage earner. (55 letters)

"""
