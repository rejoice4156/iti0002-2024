"""Create dictionary with names and years."""


def create_years_dict(people_list: list, year_list: list) -> dict:
    """
    Return a dictionary with keys as names and values as years.

    people_list = ["Mari", "Kalle"]
    year_list = [2005, 2006]

    create_years_dict(["Mari", "Kalle"], [2005, 2006]) => {"Mari": 2005, "Kalle": 2006}

    :param people_list: list of peoples' names.
    :param year_list: list of years they were born in.

    :return: Dictionary with keys as names and values as years.
    """
    years_dict = {}
    index = 0
    for people in people_list:
        years_dict[people] = year_list[index]
        index += 1
    return years_dict


if __name__ == "__main__":
    print(create_years_dict(["Mari", "Kalle"], [2005, 2006]))  # => {"Mari": 2005, "Kalle": 2006}
    print(create_years_dict(["Karl"], [2003]))  # => {"Karl": 2003}
    print(create_years_dict(["Liisa", "Anna", "Bob"], [2007, 2005, 2006]))
    # => {"Liisa": 2007, "Anna": 2005, "Bob": 2006}
