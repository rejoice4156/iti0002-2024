"""Create repeated list."""


def create_repeated_list(elements: list, repetition: int) -> list:
    """
    Create a list where the initial list's elements are repeated the amount of times given as the second argument .

    create_repeated_list([1, 2], 2) => [1, 2, 1, 2]
    create_repeated_list([1], 5) => [1, 1, 1, 1, 1]
    create_repeated_list([1, 2], 0) => []
    """
    elements *= repetition
    return elements


if __name__ == '__main__':
    print(create_repeated_list([1, 2], 2))
    print(create_repeated_list([1], 5))
    print(create_repeated_list([1, 2], 0))
