"""Count symbols appearances."""


def count_symbol_appearances(stringy: str) -> dict:
    """
    Return dict where key is the character and the value is the count this character is present in the string.

    count_symbol_appearances("hello hi") => {'h': 2, 'e': 1, 'l': 2, 'o': 1, ' ': 1, 'i': 1}

    :param stringy: string to be processed.
    :return: dictionary with character counts.
    """
    dictionary = {}
    for char in stringy:
        if char not in dictionary:
            dictionary[char] = stringy.count(char)
    return dictionary


if __name__ == "main":
    print(count_symbol_appearances("hello hi"))  # => {'h': 2, 'e': 1, 'l': 2, 'o': 1, ' ': 1, 'i': 1}
    print(count_symbol_appearances("ago"))  # => {'a' : 1, 'g' : 1, 'o' : 1}
    print(count_symbol_appearances("hüsteeriline"))  # => {'h' : 1, 'ü' : 1, 's' : 1, 't' : 1, 'e' : 3, 'r' : 1, 'i' : 2, 'l' : 1, 'n' : 1}
