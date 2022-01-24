def getEven(list1=[]):
    """
    Return a list containing even elements which is in list1

    >>> getEven([3, 53, 7654, 453, 324, 435, 234, 4, 42, 24, 1])
    [7654, 324, 234, 4, 42, 24]
    >>> common_elements()
    []
    """
    return [i for i in list1 if not i % 2]
