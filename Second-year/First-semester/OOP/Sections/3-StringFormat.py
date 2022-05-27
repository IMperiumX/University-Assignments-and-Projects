"""
Object Oriented Programming (OOP) >> (CS213).

Description: Write a python program to get a string made of the first 2 and
the last 2 chars from a given string. if the string length is less than 2
return instead an empty string.

PS:
String Slicing[start:end:<Steps>]: Start backwords if the number is negative.
 Y  u  s  u  f
 1  2  3  4  5
-5 -4 -3 -2 -1



functions: len() get the number of char in a string, start from 1 if not empty
string.

"""

# Structre Programming Style...

sample = str(input("Enter a String: "))

if len(sample) > 1:
    print(sample[:2] + sample[-2:])
else:
    print("''")


# Fucntional Style...


# def ValidSample(sample):
#     empty = True
#     if len(sample) < 1:
#         empty = False

#     return empty


# def SampleSlice(sample):
#     if ValidSample(sample):
#         return sample[:2] + sample[-2:]
#     else:
#         return "''"


# def main():
#     print(SampleSlice(sample))


# if __name__ == '__main__':
#     main()
