words = input("Enter list of words separated with spaces: ").split(" ")

def longest_word(words: str) -> str:
    """longest_word takes a list of words and return
    the longest word and the length of the longest one

        :param words: list of words
        :type word: str
        :return: str and integer -> (word length)
        :rtype: str
    """
    lw = max(words, key=len)
    return f"""Longest word: {lw}
Length of the longest word: {len(lw)}
                """


