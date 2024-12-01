"""Contains digit."""


def contains_digit(some_string: str) -> bool:
    """
    Check if a given string contains at least one digit.

    :param some_string: given string
    :return: Return True if the input string contains a digit, False otherwise.
    """
    for char in some_string:
        if char.isdigit():
            return True
    return False


if __name__ == '__main__':
    print(contains_digit("!No.Digits/Here123?"))
