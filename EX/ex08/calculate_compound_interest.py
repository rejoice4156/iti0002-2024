"""Calculate compound interest."""


def calculate_compound_interest(amount: int, years: int, rate: int) -> float:
    """
    Calculate compound interest.

    print(calculate_compound_interest(100, 2, 2)) => 104.04
    print(calculate_compound_interest(2000, 6, 8)) => 3173.748645888

    :param amount: starting amount
    :param years: number of years
    :param rate: interest rate per year
    :return: Final amount.
    """
    for i in range(years):
        amount += amount * rate / 100
    return amount


if __name__ == '__main__':
    print(calculate_compound_interest(100, 2, 2))
    print(calculate_compound_interest(2000, 6, 8))
