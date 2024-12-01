"""Get middle element of list."""


def get_middle_element_of_list(elements: list) -> any:
    """
    Return the middle element in a list with an odd number of elements.

    The list always has an odd number of elements.
    get_middle_element_of_list([1]) = 1
    get_middle_element_of_list([1, 2, 3]) => 2
    get_middle_element_of_list(["a", "b", "c"]) => "b"
    """
    return elements[len(elements) // 2]


if __name__ == "__main__":
    print(get_middle_element_of_list([1]))
    print(get_middle_element_of_list([1, 2, 3]))
    print(get_middle_element_of_list(["a", "b", "c"]))
