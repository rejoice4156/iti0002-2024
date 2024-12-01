"""Reverse a list."""


def reverse_list(elements: list) -> list:
    """
    Return reversed list.

    reverse_list([1, 2, 3]) => [3, 2, 1]
    reverse_list(["a", "b"]) => ["b", "a"]
    """
    elements.reverse()
    return elements


if __name__ == '__main__':
    print(reverse_list([1, 2, 3]))
    print(reverse_list(["a", "b"]))
