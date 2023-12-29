"""
Object Oriented Programming (OOP) >> (CS213).

Description: Write a  Python program to add "ing" at the end of a given
string (length should be at least 3). if the given string already ends
with 'ing' then add 'ly' instead. if the string length of the given string is
less than 3, leave it unchged.


str.endwith(): Return True if the string ends with 'ing' that also make sure string's length at least 3.



"""


String = str(input("Enter a String: "))

Condition = String.endswith('ing')


if len(String) < 3:
    print(String)

elif String.endswith('ing'):
    print(f'{String}ly')

else:
    print(f'{String}ing')
