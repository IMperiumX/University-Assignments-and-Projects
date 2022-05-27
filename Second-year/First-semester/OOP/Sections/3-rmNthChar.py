"""
Object Oriented Programming (OOP) >> (CS213).

Description: Write a Python program to remove the Nth Index chracter from a
nonempty string.


Using Slicing


"""

String = str(input("Enter a string: "))

StrLength = len(String) - 1  # ( -1 ) so we could start counting from 0 index

i = int(input(f"Enter chracter's index to be removed(0, {StrLength}): "))

# Using first and last part of a string and skipping the character by doing (i + 1).
first = String[:i]
last = String[i + 1 :]

Final = first + last

print(f"{String} >> {Final}")
