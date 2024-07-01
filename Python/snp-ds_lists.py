"""
5.1. More on Lists

The list data type has some more methods. Here are all of the methods of list objects:

list.append(x)

    Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)

    Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)

    Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)

    Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])

    Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. It raises an IndexError if the list is empty or the index is outside the list range.

list.clear()

    Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])

    Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

    The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)

    Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)

    Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()

    Reverse the elements of the list in place.

list.copy()

    Return a shallow copy of the list. Equivalent to a[:].

An example that uses most of the list methods:
>>>

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.count('apple')
2

fruits.count('tangerine')
0

fruits.index('banana')
3

fruits.index('banana', 4)  # Find next banana starting at position 4
6

fruits.reverse()

fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

fruits.append('grape')

fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

fruits.sort()

fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

fruits.pop()
'pear'

You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed – they return the default None. [1] This is a design principle for all mutable data structures in Python.

Another thing you might notice is that not all data can be sorted or compared. For instance, [None, 'hello', 10] doesn't sort because integers can't be compared to strings and None can't be compared to other types. Also, there are some types that don't have a defined ordering relation. For example, 3+4j < 5+7j isn't a valid comparison.
5.1.1. Using Lists as Stacks

The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index. For example:
>>>

stack = [3, 4, 5]

stack.append(6)

stack.append(7)

stack
[3, 4, 5, 6, 7]

stack.pop()
7

stack
[3, 4, 5, 6]

stack.pop()
6

stack.pop()
5

stack
[3, 4]

5.1.2. Using Lists as Queues

It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. For example:
>>>

from collections import deque

queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")           # Terry arrives

queue.append("Graham")          # Graham arrives

queue.popleft()                 # The first to arrive now leaves
'Eric'

queue.popleft()                 # The second to arrive now leaves
'John'

queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])

5.1.3. List Comprehensions

List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

For example, assume we want to create a list of squares, like:
>>>

squares = []

for x in range(10):

    squares.append(x**2)


squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Note that this creates (or overwrites) a variable named x that still exists after the loop completes. We can calculate the list of squares without any side effects using:

squares = list(map(lambda x: x**2, range(10)))

or, equivalently:

squares = [x**2 for x in range(10)]

which is more concise and readable.

A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it. For example, this listcomp combines the elements of two lists if they are not equal:
>>>

[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

and it's equivalent to:
>>>

combs = []

for x in [1,2,3]:

    for y in [3,1,4]:

        if x != y:

            combs.append((x, y))


combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

Note how the order of the for and if statements is the same in both these snippets.

If the expression is a tuple (e.g. the (x, y) in the previous example), it must be parenthesized.
>>>

vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled

[x*2 for x in vec]
[-8, -4, 0, 4, 8]

# filter the list to exclude negative numbers

[x for x in vec if x >= 0]
[0, 2, 4]

# apply a function to all the elements

[abs(x) for x in vec]
[4, 2, 0, 2, 4]

# call a method on each element

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']

[weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']

# create a list of 2-tuples like (number, square)

[(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# the tuple must be parenthesized, otherwise an error is raised

[x, x**2 for x in range(6)]
  File "<stdin>", line 1
    [x, x**2 for x in range(6)]
     ^^^^^^^
SyntaxError: did you forget parentheses around the comprehension target?

# flatten a list using a listcomp with two 'for'

vec = [[1,2,3], [4,5,6], [7,8,9]]

[num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]

List comprehensions can contain complex expressions and nested functions:
>>>

from math import pi

[str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']

5.1.4. Nested List Comprehensions

The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.

Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
>>>

matrix = [

    [1, 2, 3, 4],

    [5, 6, 7, 8],

    [9, 10, 11, 12],

]

The following list comprehension will transpose rows and columns:
>>>

[[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

As we saw in the previous section, the inner list comprehension is evaluated in the context of the for that follows it, so this example is equivalent to:
>>>

transposed = []

for i in range(4):

    transposed.append([row[i] for row in matrix])


transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

which, in turn, is the same as:
>>>

transposed = []

for i in range(4):

    # the following 3 lines implement the nested listcomp

    transposed_row = []

    for row in matrix:

        transposed_row.append(row[i])

    transposed.append(transposed_row)


transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

In the real world, you should prefer built-in functions to complex flow statements. The zip() function would do a great job for this use case:
>>>

list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

See Unpacking Argument Lists for details on the asterisk in this line.
5.2. The del statement

There is a way to remove an item from a list given its index instead of its value: the del statement. This differs from the pop() method which returns a value. The del statement can also be used to remove slices from a list or clear the entire list (which we did earlier by assignment of an empty list to the slice). For example:
>>>

a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]

a
[1, 66.25, 333, 333, 1234.5]

del a[2:4]

a
[1, 66.25, 1234.5]

del a[:]

a
[]

del can also be used to delete entire variables:
>>>

del a

Referencing the name a hereafter is an error (at least until another value is assigned to it). We'll find other uses for del later.
"""