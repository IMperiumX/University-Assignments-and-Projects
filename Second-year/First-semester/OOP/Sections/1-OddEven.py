"""
Object Oriented Programming (OOP) >> (CS213).

Description: Tha program asks the user for a number. Depending on wherher the
number is even or odd print ou an appropriate message to the use.

extras: if the number is multiple of 4, print out a diifferent message. Ask
the user for two numbers: one number to check(call it num) and one number to
divide by(check). if check divides evenly into num, tell that to the user. if
no, print different appropriate message.

Hint: how does an even / odd number read differently when divide by 2?



"""

# Ask user to enter an integer number, store it in userinput variable
userinput = int(input("Enter a integer number: "))


# Module operator(%) return a number other that 0 if the number is odd, so the
# condition is True.

if userinput % 2:
    print(f"Number {userinput} is odd.")

# 44 % 4 = 0 means divisor of 4, so we use the keyword not to make the condition 1 or True!.
elif not (userinput % 4):
    print(f"The number {userinput} is divided by 4.")

else:
    print(f"Number {userinput} is even.")
