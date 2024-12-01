"""Longer string first."""


def longer_string_first(first_string: str, second_string: str) -> str:
    """Return longer string in front and the shorter string after that."""
    if len(first_string) >= len(second_string):
        return first_string + second_string
    else:
        return second_string + first_string


if __name__ == '__main__':
    print(longer_string_first('abc', 'defg'))
