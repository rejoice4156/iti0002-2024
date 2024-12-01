"""Swap edge elements."""


def swap_edge_elements(elements: list) -> list:
    """
    Return a list where the first and last element of the initial list are swapped.

    swap_edge_elements([1, 2, 3]) => [3, 2, 1]
    swap_edge_elements([1, 2]) => [2, 1]
    swap_edge_elements([1, 2, 1, 4]) => [4, 2, 1, 1]
    swap_edge_elements(["foo", "bar", "pub"]) => ["pub", "bar", "foo"]

    """
    updated_elements = []  # Create an empty array.
    updated_elements.append(elements[-1])  # Append the last element from elements to updated_elements.
    for element in elements[1:-1]:  # Loop through elements from 1 to -1 (not included).
        updated_elements.append(element)  # Append those elements to updated_elements.
    updated_elements.append(elements[0])  # Append the first element from elements to updated_elements.
    return updated_elements  # Return the finalised updates_elements array.


if __name__ == "__main__":
    print(swap_edge_elements([1, 2, 3]))
    print(swap_edge_elements([1, 2]))
    print(swap_edge_elements([1, 2, 1, 4]))
    print(swap_edge_elements(["foo", "bar", "pub"]))
