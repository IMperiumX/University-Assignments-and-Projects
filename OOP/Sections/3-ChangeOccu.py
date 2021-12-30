"""
Object Oriented Programming (OOP) >> (CS213).

Description: Write a Python program to get a string from a given string where
all occurences of its char have been changed to "$", except the first char
itself.

Using slicing + replace()


Author: yusufadell

"""


String = str(input("Enter a String: "))

# printing original string
print(f"The original string is : {String}")

print(70 * "-")


First_char = String[0]

String = First_char + String[1:].replace(First_char, "$")

# printing result
print(f"Replaced String : {String}")
