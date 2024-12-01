"""Convert list to set."""


def convert_list_to_set(list_a: list) -> set:
    """
    Take a list, convert it to a set and return it.

    convert_list_to_set([1, 2, 3, 1]) => {1, 2, 3}
    convert_list_to_set([1, 2, 3, 4]) => {1, 2, 3, 4}

    :param list_a: given list
    :return: set made from given list.
    """
    return set(list_a)


if __name__ == "main":
    # run this file to test the function
    print(convert_list_to_set([1, 2, 3, 1]))  # {1, 2, 3}
    print(convert_list_to_set([1, 2, 3, 4]))  # {1, 2, 3, 4}
