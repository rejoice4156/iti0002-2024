"""Get first n symbols of a string."""


def get_first_n_symbols(test_string: str, number: int) -> str:
    """Return the first n characters of the string."""
    return test_string[:number]


if __name__ == '__main__':
    print(get_first_n_symbols('hello world', 5))
