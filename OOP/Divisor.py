"""
Object Oriented Programming (OOP) >> (CS213).

Description: Create a program that asks the user fir a number and then prints
out a list of all the divisors ofthe number.

Divisor is a number that divides evenly into another number. 
for example, 13 is a divisor of 26 because 26/13 have no remonder.

Author: yusufadell

"""
import math


# The Dump Way to solve it.

userinput = int(input("Enter an integer to get all it's divisors: "))

ans = []
for i in range(1, int(math.sqrt(userinput)) + 1):
    if userinput % i == 0:
        ans.append(i)

print(f"Divisors of {userinput} are {ans}")


# def divisorGenerator(n):
#     large_divisors = []
#     for i in range(1, int(math.sqrt(n) + 1)):
#         if n % i == 0:
#             yield i
#             if i * i != n:
#                 large_divisors.append(n / i)
#     for divisor in reversed(large_divisors):
#         yield divisor


# print(list(divisorGenerator(userinput)))

# Because, once you have a list of elements between 1..10, you can generate
# any of the elements between 11..100 trivialy. You get {1, 2, 4, 5, 10}.
# Divide 100 by each of these elements and you {100, 50, 20, 25, 10}.
