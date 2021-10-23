userinput = input("Enter Two number seperated by spaces: ").split(" ")

userinput = [int(i) for i in userinput]


print(f"Addition: {sum(userinput)}")
print(
    f"substraction: {userinput[0] - userinput[1]} or {abs(userinput[1] - userinput[0])}"
)
print(f"exponentionl: {userinput[0] ** userinput[1]} or {userinput[1] ** userinput[0]}")
print(f"Division: {userinput[0] / userinput[1]} or {userinput[1] / userinput[0]}")
