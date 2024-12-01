"""Count unique elements in the list."""


def count_unique_elements(input_list: list) -> int:
    """
    Count unique elements in the list.

    Hint: set only has unique elements.

    Hint: no loop required

    count_unique_elements([1, 2, 3]) => 3
    count_unique_elements([1, 1, 1]) => 1
    count_unique_elements([]) => 0
    """
    return len(set(input_list))


if __name__ == "main":
    # run this file to test the function
    print(count_unique_elements([1, 2, 3]))  # 3
    print(count_unique_elements([1, 2, 1]))  # 2
