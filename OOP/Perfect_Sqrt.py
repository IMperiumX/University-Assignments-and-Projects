"""
Object Oriented Programming (OOP) >> (CS213).

Description: Write a function that takes a list of numbers and two numberss X,
Y as parameters Check which of the items in list are perfect squares(integers
that are squares of another integer )in a give range [X,Y]


Author: yusufadell

modules: math>> using sqrt function from math module to calculate the square
root of a number and return a float.
"""


from math import sqrt


def PerfectSqrt(List: list, X: int, Y: int):
    List = List[X:Y]
    ans = [i for i in List if int(sqrt(i)) ** 2 == i]
    print(ans)


List = [2, 4, 26, 76, 34, 16]
PerfectSqrt(List, 0, 4)
