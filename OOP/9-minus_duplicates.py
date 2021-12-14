list_with_duplicates = [1, 2, 56, 123, 56, 435, 324, 87, 2, 123]


def minus_dubl(nums: list):
    """minus_dubl: take a list of numbers and
    return it without any dublicates.

    :param nums: List with numbers
    :type nums: list
    """
    nums = list(set(nums))
    print(f"List With no dublicates: {nums}")


