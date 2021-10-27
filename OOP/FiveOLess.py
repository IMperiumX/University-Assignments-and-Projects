"""
Object Oriented Programming (OOP) >> (CS213).

Description: Write a program that prints out all the element of the list that
are less than 5.

Take a list, say for example this one:
a = [1,2,3,4,5,6,7,8,9,99,75,345]
>> [1,2,3,4]


Author: yusufadell

"""

userinput = input("Enter numbers seperated by space: ")


# Ambiguous Way Using list comprehension and not recommended!.
tmp = userinput.split(" ")
List = [int(i) for i in tmp]
ans = [i for i in List if i < 5]

print(ans)

# try:
#     tmp = userinput.split(" ")
#     List = [int(i) for i in tmp] Using list comprehension
#     List = []
#     for i in tmp:
#         List.append(int(i))

#     ans = [i for i in List if i < 5]
#     ans = []
#     for i in List:
#         if i < 5:
#             ans.append(i)

#     # The function sorted(): sort the list before print it to the user
#     if len(ans) == 0:
#         print(f"There is no numbers less than 5 in {sorted(List)}")
#     else:
#         print(f"{sorted(ans)} numbers less than 5 in {sorted(List)}")

# except Exception as e:
#     print("Enter a valid Integer!")
