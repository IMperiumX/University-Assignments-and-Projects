'''
Object Oriented Programming (OOP) >> (CS213).

Description: Program asks the user for 2 numbers and do four different
Arithmetic operations, and display the result/


Author: yusufadell


'''


# alternatively use map(int, input("Enter First number").split(""))

num1 = int(input("Enter First number"))
num2 = int(input("Enter Second number"))


# Using Format String to act as a template / placeholder for variables,
# Notices f" ".

addition = num1 + num2
print(f"Addition of {num1} + {num2} = {addition}")


multiple = num1 * num2
print(f"Multiplication of {num1} * {num2} = {multiple}")


subtraction = max(num2, num1) - min(num2, num1)
print(f"subtraction of {num1} - {num2} = {subtraction} ")


Power = num1 ** num2
print(f"{num1} to the power of {num2} = {Power}")
