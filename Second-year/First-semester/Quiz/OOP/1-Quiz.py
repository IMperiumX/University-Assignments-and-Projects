# 1- What is the first output?

for i in range(10):
    if (i + 1) % 2 == 0:
        print("even")
    else:
        print("odd")

# and: "odd"

# ----------------------------------------------------------

# 2- What is the output?

d = {0: "a", 1: "b", 2: "c"}
for i in d:
    print(i)

# and: 0   1   2

# ----------------------------------------------------------


t = (1, 2, 3)
print(len(t))

# and: 3


# ----------------------------------------------------------


def add(a, b, c):
    return str(a) + str(b) + str(c)


print(add(1, 2, 3))

# and: 123


# ----------------------------------------------------------


i = 1
while 1 < 3:
    print("good")
    break

# and: good

# ----------------------------------------------------------

List = [1, 2, 3, 4, 5]
print(List)

# and: [1, 2, 3, 4, 5]

# ----------------------------------------------------------

list1 = [1, 2, 3, 4]
list2 = list(list1)
list1.append(5)
print(list2)

# and: [1, 2, 3, 4]

# ----------------------------------------------------------


# What is the data type of this object Var=(2)?

Var = 2
print(type(Var))

# and: int


# ----------------------------------------------------------


def convert(a, b, c):
    return len(a) + len(b) + c


print(convert({2, 3, 49}, (2, 555, 1, 5, 7), 5000))
# and: 3 + 5 + 5000 =5008
