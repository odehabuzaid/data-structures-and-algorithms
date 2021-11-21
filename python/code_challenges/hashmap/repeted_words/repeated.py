import string

from ..hash_map import HashTable


def repeated_word(sentence: str) -> str:
    hash_table = HashTable()
    # region docs
    """
    finds the first word that occur more than once in a string

    Args:
        sentence (str): sentences as string of length n

    Returns:
        str: the first word that is repeated more than once in the given string
    """
    # endregion

    for word in sentence.lower().split():

        word = word.strip(string.punctuation)

        try:

            hash_table.get(word)

            return word

        except:
            hash_table.add(word, word)
