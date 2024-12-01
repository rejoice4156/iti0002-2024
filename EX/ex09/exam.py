"""Sum numbers between elements 2 and 5."""


def sum_between_25(numbers: list) -> int:
    """
    Return the sum of the numbers in the array which are between 2 and 5.

    Summing starts from 2 (not included) and ends at 5 (not included).
    The section can contain 2 (but cannot 5 as this would end it).
    There can be several sections to be summed.

    sum_between_25([1, 3, 6, 7]) => 0
    sum_between_25([1, 2, 3, 4, 5, 6]) => 7
    sum_between_25([1, 2, 11, 5, 6]) => 11
    sum_between_25([1, 2, 3, 4, 6, 6]) => 19
    sum_between_25([1, 3, 3, 4, 5, 6]) => 0
    sum_between_25([1, 2, 3, 4, 5, 6, 1, 2, 9, 5, 6]) => 16
    sum_between_25([1, 2, 3, 2, 5, 5, 3, 5]) => 5
    """
    sum_of_numbers = 0
    control_number = 0
    for number in numbers:
        if number == 5:
            control_number = 0
        if control_number == 1:
            sum_of_numbers += number
        if number == 2:
            control_number = 1
    return sum_of_numbers


if __name__ == '__main__':
    print(sum_between_25([1, 3, 6, 7]))  # 0
    print(sum_between_25([1, 2, 3, 4, 5, 6]))  # 7
    print(sum_between_25([1, 2, 11, 5, 6]))  # 11
    print(sum_between_25([1, 2, 3, 2, 5, 5, 3, 5]))  # 5
    print(sum_between_25([1, 2, 3, 4, 6, 6]))  # 19
    print(sum_between_25([1, 3, 3, 4, 5, 6]))  # 0
    print(sum_between_25([1, 2, 3, 4, 5, 6, 1, 2, 9, 5, 6]))  # 16
    print(sum_between_25([2, 2, 2, 2, 2, 2, 2]))  # 12
    print(sum_between_25([]))  # 0
    print(sum_between_25([1, 6, 7, 8]))  # 0
    print(sum_between_25([2, 3, 4, 6]))  # 13
    print(sum_between_25([2, 3, 5, 2, 4, 5]))  # 7
    print(sum_between_25([2, 3, 4, 5, 5, 6]))  # 7
    print(sum_between_25([2, 5, 2, 5, 2, 5]))  # 0
    print(sum_between_25([2, 3, 5, 2, 6, 5]))  # 9
    print(sum_between_25([1, 2, 6, 2, 5]))  # 8
    print(sum_between_25([1, 2, 3]))  # 3
    print(sum_between_25([2, 2, 3, 5, 5]))  # 5
    print(sum_between_25([2, 2, 5, 2, 2, 5]))  # 4
    print(sum_between_25([2, 2]))  # 2
