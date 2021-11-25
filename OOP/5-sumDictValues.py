# Write a Python program to sum all the items(keys & values) in a dictionary.

d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


print(sum([sum(i) for i in d.items()]))

# OR


def sumValues(dictionary):
    dict_values = dictionary.values()
    return sum(dict_values)


def sumKeys(dictionary):
    dict_keys = dictionary.keys()
    return sum(dict_keys)


def sumItems(keys, values):
    return keys + values


def main():
    keys = sumKeys(d)
    values = sumValues(d)
    return sumItems(keys, values)


print(main())
