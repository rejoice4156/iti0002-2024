"""Capitalize letters in text."""


def capitalize_letters(text: str) -> str:
    """
    If a letter is present in given string in both lowercase and uppercase, capitalize all occurrences of the letter.

    Examples:
    capitalize_letters("") -> ""
    capitalize_letters("abbA") -> "AbbA"
    capitalize_letters("abBa") -> "aBBa"
    capitalize_letters("AbBa") -> "ABBA"
    capitalize_letters("AbbA") -> "AbbA
    capitalize_letters("abba") -> "abba"
    capitalize_letters("ABBA") -> "ABBA"

    :param text: given text
    :return: capitalized text
    """
    # Create a set containing all unique letters from the text.
    lower_case = set(text.lower())
    # Create an empty set to store all letters that appear in both lower- and uppercase.
    both_cases = set()
    # From the set of unique letters in the text, find which letters appear in both lower- and uppercase.
    for letter in lower_case:
        if letter.lower() in text and letter.upper() in text:
            # Add the lowercase version of the letter to both_cases set.
            both_cases.add(letter.lower())
    # Create new empty string named result.
    result = ""
    # Go through all letters in the original text string.
    for letter in text:
        # Check if any given letter in lowercase form appears in the both_cases set.
        if letter.lower() in both_cases:
            # If yes, then add the uppercase version of it to the result.
            result += letter.upper()
        else:
            # If not, then just add the letter as it was to the result.
            result += letter
    return result


if __name__ == '__main__':
    print(capitalize_letters(""))
    print(capitalize_letters("abbA"))
    print(capitalize_letters("abBa"))
    print(capitalize_letters("AbBa"))
    print(capitalize_letters("AbbA"))
    print(capitalize_letters("abba"))
    print(capitalize_letters("ABBA"))
