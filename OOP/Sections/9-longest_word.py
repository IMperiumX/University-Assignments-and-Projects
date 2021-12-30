words = input("Enter list of words seperated with spaces: ").split(" ")

def longest_word(words: str) -> str:
    """longest_word takes a list of words and return
    the longest word and the length of the longest one

        :param words: list of words
        :type word: str
        :return: str and integer -> (word lenght)
        :rtype: str
    """
    lw = max(words, key=len)
    template = f"""Longest word: {lw}
Length of the longest word: {len(lw)}
                """
    return template


