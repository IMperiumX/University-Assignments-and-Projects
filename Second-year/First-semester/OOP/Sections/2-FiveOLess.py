"""
Object Oriented Programming (OOP) >> (CS213).

Description: Write a program that prints out all the element of the list that
are less than 5.

Take a list, say for example this one:
a = [1,2,3,4,5,6,7,8,9,99,75,345]
>> [1,2,3,4]




"""

userinput = input("Enter numbers separated by space: ")


# Uncomment the following code to run the program.


try:
    tmp = userinput.split(" ")
    # List = [int(i) for i in tmp]  # Using list comprehension.
    List = []
    for i in tmp:
        List.append(int(i))

    # and = [i for i in List if i < 5] # list comprehension again.
    and = []
    for i in List:
        if i < 5:
            and.append(i)

    # The function sorted(): sort the list before print it to the user
    if len(and) == 0:
        print(f"There is no numbers less than 5 in {sorted(List)}")
    else:
        print(f"{sorted(and)} numbers less than 5 in {sorted(List)}")

except Exception as e:
    print("Enter valid numbers!")


# # Ambiguous Way Using list comprehension and not recommended!.

# and = [i for i in [int(i) for i in userinput.split(" ")] if i < 5]

# print(and)
