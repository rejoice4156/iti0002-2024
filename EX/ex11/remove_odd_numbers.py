"""Remove odd numbers."""


def remove_odd_numbers(numbers: tuple) -> tuple:
    """
    Return a tuple where all the odd numbers are removed from the tuple received as input.

    The order of the elements should remain the same.

    remove_odd_numbers((1, 2, 3)) => (2, )
    remove_odd_numbers((1, 5, 3)) => ()
    remove_odd_numbers((2, 4, 6)) => (2, 4, 6)
    """
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return tuple(even_numbers)


if __name__ == "main":
    print(remove_odd_numbers((1, 2, 3)))  # => (2, )
    print(remove_odd_numbers((1, 5, 3)))  # => ()
    print(remove_odd_numbers((2, 4, 6)))  # => (2, 4, 6)
