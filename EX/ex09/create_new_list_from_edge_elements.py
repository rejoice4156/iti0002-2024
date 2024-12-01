"""Create new list from edge elements."""


def create_new_list_from_edge_elements(elements: list) -> list:
    """
    Create a list, which is the input list without the first and the last element.

    create_new_list_from_edge_elements([1, 2, 3]) => [2]
    create_new_list_from_edge_elements([1, 3]) => []
    create_new_list_from_edge_elements([1, 3, 6, 7]) => [3, 6]
    create_new_list_from_edge_elements(["a", "b", "b", "a"]) => ["b", "b"]
    """
    new_list_from_edge_elements = elements[1:-1]
    return new_list_from_edge_elements


if __name__ == "__main__":
    print(create_new_list_from_edge_elements([1, 2, 3]))
    print(create_new_list_from_edge_elements([1, 3]))
    print(create_new_list_from_edge_elements([1, 3, 6, 7]))
    print(create_new_list_from_edge_elements(["a", "b", "b", "a"]))
