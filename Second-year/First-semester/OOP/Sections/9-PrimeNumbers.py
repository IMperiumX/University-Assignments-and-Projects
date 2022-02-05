# Program to check if a number is prime or not

num = int(input("Enter a number to test if Prime:"))

# To take input from the user
#num = int(input("Enter a number: "))


# prime numbers are greater than 1
def get_prime(num):
    
    # define a flag variable
    flag = False
    if num > 1:
    # check for factors
        for i in range(2, num):
            if (num % i) == 0:
            # if factor is found, set flag to True
                flag = True
            # break out of loop
                break
    return flag

flag = get_prime(num)

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")