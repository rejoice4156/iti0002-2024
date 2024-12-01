"""Multiplication of numbers in the range."""


def multiplication_of_numbers_in_range(start: int, end: int) -> int:
    """
    Multiply all numbers between start and end (both included).

    print(multiplication_of_numbers_in_range(1, 3)) => 1 * 2 * 3 = 6
    print(multiplication_of_numbers_in_range(4, 14)) => 14529715200
    print(multiplication_of_numbers_in_range(0, 7)) => 0

    :param start: start of inclusive range
    :param end: end of inclusive range
    :return: product of all numbers between start and end
    """
    answer = 1
    for i in range(start, end + 1):
        answer *= i
    return answer


if __name__ == '__main__':
    print(multiplication_of_numbers_in_range(1, 3))
    print(multiplication_of_numbers_in_range(4, 14))
    print(multiplication_of_numbers_in_range(0, 7))
