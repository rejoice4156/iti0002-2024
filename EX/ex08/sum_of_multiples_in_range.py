"""Sum of multiples in range."""


def sum_of_multiples_in_range(n: int, end: int) -> int:
    """
    Return sum of numbers which are multiples of n between 0 and end (included).

    print(sum_of_multiples_in_range(3, 10)) => 3 + 6 + 9 = 18
    print(sum_of_multiples_in_range(7, 10)) => 7
    print(sum_of_multiples_in_range(11, 10)) => 0

    :param n: multiplier
    :param end: inclusive upper limit of range
    :return: Sum of numbers which are multiples of n between 0 and end.
    """
    sum_of_multiples = 0
    for i in range(0, end + 1):
        if i % n == 0:
            sum_of_multiples += i
    return sum_of_multiples


if __name__ == '__main__':
    print(sum_of_multiples_in_range(3, 10))
    print(sum_of_multiples_in_range(7, 10))
    print(sum_of_multiples_in_range(11, 10))
