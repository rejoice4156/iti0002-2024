"""Remove sixes."""


def remove_sixes(set_a: set) -> set:
    """
    Take a set of numbers and remove the number six from it if its there, return the set without sixes.

    remove_sixes({1, 2, 3, 4, 5, 6, 7, 8, 9}) => {1, 2, 3, 4, 5, 7, 8, 9}
    remove_sixes({1, 5, 7}) => {1, 5, 7}

    :param set_a: given set
    :return: set without sixes.
    """
    set_a.discard(6)
    return set_a


if __name__ == "main":
    # run this file to test the function
    print(remove_sixes({1, 2, 3, 4, 5, 6, 7, 8, 9}))  # {1, 2, 3, 4, 5, 7, 8, 9}
    print(remove_sixes({1, 5, 7}))  # {1, 5, 7}
