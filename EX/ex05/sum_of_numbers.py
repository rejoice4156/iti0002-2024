"""Sum of numbers."""


def sum_of_numbers(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


if __name__ == '__main__':
    a = (int(input("Enter a number: ")))
    b = (int(input("Enter another number: ")))
    print(sum_of_numbers(a, b))
