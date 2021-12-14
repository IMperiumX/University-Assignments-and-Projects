word = input("Enter any word to get its plural: ")


def plural(word):
    """plural  Converts a word to its plural form.

    :param word: Any singular word
    :type word: 'str'
    :return: Plural word
    :rtype: 'str'
    """

    if word.endswith("fe"):
        # wolf -> wolves
        return word[:-2] + "ves"
    elif word.endswith("f"):
        # knife -> knives
        return word[:-1] + "ves"
    elif word.endswith("o"):
        # potato -> potatoes
        return word + "es"
    elif word.endswith("us"):
        # cactus -> cacti
        return word[:-2] + "i"
    elif word.endswith("on"):
        # criterion -> criteria
        return word[:-2] + "a"
    elif word.endswith("y"):
        # community -> communities
        return word[:-1] + "ies"
    elif word[-1] in "sx" or word[-2:] in ["sh", "ch"]:
        return word + "es"
    elif word.endswith("an"):
        return word[:-2] + "en"
    else:
        return word + "s"


