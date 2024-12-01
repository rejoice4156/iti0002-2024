"""Create new list with added number."""


def create_new_list_with_added_number(numbers: list, number: int) -> list:
    """
    Return a new list with the number added to it.

    Do not modify the existing list.
    add_element_into_list([1, 2, 3], 4) => [1, 2, 3, 4]
    """
    original_list = numbers
    list_with_new_number = [number]
    new_list_with_added_number = original_list + list_with_new_number
    return new_list_with_added_number


if __name__ == '__main__':
    print(create_new_list_with_added_number([1, 2, 3, 4], 4))
