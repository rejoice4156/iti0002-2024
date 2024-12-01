"""Create list of elements."""


def create_list_of_elements(a: int, b: int) -> list:
    """
    Return a list of the two elements a and b (in that order).

    create_list_of_two_elements(1, 2) => [1, 2]
    create_list_of_two_elements(81, 72) => [81, 72]
    """
    two_elements = [a, b]
    return two_elements


if __name__ == '__main__':
    print(create_list_of_elements(1, 2))
    print(create_list_of_elements(81, 72))
