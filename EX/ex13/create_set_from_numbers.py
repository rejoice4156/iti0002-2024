"""Create set from numbers."""


def create_set_from_numbers(a: int, b: int, c: int) -> set:
    """
    Create set from three integers.

    create_set_from_numbers(1, 2, 3) => {1, 2, 3}
    create_set_from_numbers(1, 2, 1) => {1, 2}
    create_set_from_numbers(1, 1, 1) => {1}
    """
    return {a, b, c}


if __name__ == "main":
    # run this file to test the function
    print(create_set_from_numbers(1, 2, 3))  # {1, 2, 3}
    print(create_set_from_numbers(1, 2, 1))  # {1, 2}
