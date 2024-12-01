"""Capitalize and replace letters in string."""


def modify_string(phrase: str) -> str:
    """
    Return a modified version of the string with certain letters capitalized and replaced.

    First letter of the string must be capitalized.
    All occurrences of the letters: a,e,i,o,u must be capitalized.
    """
    # Capitalize the first letter of the phrase.
    phrase = phrase.capitalize()
    # Find every instance of a, e, i, o, u in the phrase.
    for letter in ["a", "e", "i", "o", "u"]:
        # Replace each instance of that letter with it's capitalized alternative.
        phrase = phrase.replace(letter, letter.capitalize())
    return phrase


if __name__ == '__main__':
    print(modify_string("the quick brown fox jumps over the lazy dog"))
