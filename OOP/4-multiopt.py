import reprlib

userinput = input("Enter numbers seperated by spaces: ")
List = list(userinput.split(" "))


def main():
    """
    Initialize the program on a given list to do the following:
    1) display the length of list
    2) summation the list indexes
    3) order the list
    4) Reverse order (Descending)
    """
    print(f"Length --> {getLength()}")
    sumIndexes()


def getLength():
    """
    return length of a given list.
    """
    return len(List)


def sumIndexes():
    n = getLength()
    summation = 0.5 * n ** 2 - n / 2
    print(
        f"summation of the list indexes: {summation}"
    )  # Eqivalant to sum(range(n)) or (.5 * n) * (n - 1)
    orderList()


def orderList():
    NewList = [int(i) for i in List]
    NewList.sort()  # Sort the list inplace without creating a new object.
    print(f"Ordered Version: {NewList}")
    reverseOrder()


def reverseOrder():
    print(
        f"List in Descending order: {List[::-1]}"
    )  # Same list with [:] and :-1 refers to backwords steps.


if __name__ == '__main__':
    main()


# def multiopt(List):
#     """
#     Bad Function Design  --> not(Single-responsibility principle)

#     """

#     n = len(List)
#     List.sort()
#     template = f"""

# 	Lenght: {n}

# 	Sum of indexes: {sum(range(n))}

# 	Ordered list: {reprlib.repr(List)}

# 	Descending Oerder: {reprlib.repr(List[::-1])}

# 	"""
#     return template
