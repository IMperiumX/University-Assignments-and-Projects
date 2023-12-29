mylist = [1, 2, 3, 4, 5, 6, 7]

# Write a Python program to convert a list to a tuple.
mytuple = tuple(mylist)


# Write a Python program to check whether an element exists within a tuple.
mytuple.count(8)  # if 0 is the count -> element doesn't exist.


# Write a Python program to get the 4th element and 4th element from list of a tuple.
mylist[3]
mytuple[3]


# Write a Python program to print a tuple with string formatting.
tuple(list("Yusuf"))


# Write a Python program to replace last value of tuples in a list.
mylist.pop()
mylist.append(mytuple[-1])


# Write a Python program to create set difference.
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3}

# all elements that are in this set but not the others: 4
set1.difference(set2)

# Write a Python program to create a symmetric difference.

# all elements that are in exactly one of the sets: 4
set1.symmetric_difference(set2)


# Write a Python program to remove an item from a set if it is present in the set.
set1.remove(1)
