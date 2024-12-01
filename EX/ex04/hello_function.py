"""Hello function."""


def print_hello():
    """Print the string "Hello"."""
    print("Hello")


def get_hello() -> str:
    """Return the string "Hello"."""
    return "Hello"


if __name__ == '__main__':
    print_hello()
    print(get_hello())
