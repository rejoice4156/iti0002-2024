"""Find digit sum."""


def find_digit_sum(numbers: str) -> int:
    """
    Return cross sum of numbers.

    print(find_digit_sum("1234")) => 1 + 2 + 3 + 4 = 10
    print(find_digit_sum("0")) => 0
    print(find_digit_sum("4129458")) => 33

    :param numbers: string of numbers to add together
    :return: cross sum of numbers
    """
    cross_sum = 0
    for number in numbers:
        cross_sum += int(number)
    return cross_sum


if __name__ == '__main__':
    print(find_digit_sum("1234"))
    print(find_digit_sum("0"))
    print(find_digit_sum("4129458"))
