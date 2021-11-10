def common_elements(list1, list2):
    """
    Return a list containing the elements which are in both list1 and list2
    (Without duplicates)
    >>> common_elements([1,2,3,4,5,6], [3,5,7,9])
    [3, 5]
    >>> common_elements(['Yusuf', 'was', 'not', 'Here'], ['Yusuf', 'was', 'or', 'Here'])
    ['was', 'Yusuf', 'Here']
    """

    return list(set(list1).intersection(list2))

    # return [element for element in list1 if element in list2] -> List comp!

    # for element in list1:
    #     if element in list2:
    #         return list(element)
