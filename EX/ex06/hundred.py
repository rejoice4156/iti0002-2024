"""Hundred."""


def hundred(num_a: int) -> int:
    """
    Given a positive integer num_a, return 100 - num_a if it's smaller or equal to 100, else return the remainder from dividing it with 100.

    hundred(45) => 55
    hundred(100) => 0
    hundred(110) => 10

    :param num_a: given positive integer
    :return: Remainder of the calculation.
    """
    if num_a <= 100:
        return 100 - num_a
    if num_a > 0:
        return num_a % 100


if __name__ == '__main__':
    print(hundred(45))
    print(hundred(100))
    print(hundred(110))
