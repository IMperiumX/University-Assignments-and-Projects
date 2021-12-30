"""Write a Python script to generate and print dictionary that contains a
number (between 1 and n) in the form (x, x*x).

>>> Enter a number to generate a dictionary from it: 5
>>> {1: 1, 2: 4, 3: 9, 4: 16, ...}
"""

from reprlib import repr

n = int(input("Enter a number to generate a dictionary from it: "))


d = {x: x * x for x in range(1, n + 1)}


print(d)
