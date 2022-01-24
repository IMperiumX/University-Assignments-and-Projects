# Write a Python script tp print a dictionary where the keys are number between
# 1 and 15 (both included) and the values are square of keys.


d = {x: x * x for x in range(1, 16)}

# Write a python script to add a key to a dictionary
d[16] = 256


# Write a Python program to get the maximum and minimum value in a dictionary.

max(d.values())
min(d.values())


# Write a python script to merge two Python dictionaries.

d1 = {32: 32, 43: 43, 65: 53}
d1.update(d)  # {**d, **d1}
