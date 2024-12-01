"""Get hobby."""


def get_hobby(hobbies_dict: dict, name: str) -> list:
    """
    Return the hobby of the person whose name was given as the argument of the function.

    hobbies = {
    "tom": "running",
    "john": "movies",
    "ago": "swimming"
    }

    get_hobby(hobbies, "tom")  => "running"
    get_hobby(hobbies, "agO")  => "swimming"

    :param hobbies_dict: dictionary with people's hobbies.
    :param name: name of the person whose hobbies are to be returned.

    :return: Hobby of the person with the given name.
    """
    return hobbies_dict[name.lower()]


if __name__ == "main":
    # run this file to test the function
    hobbies = {
        "tom": "running",
        "john": "movies",
        "ago": "swimming"
    }
    print(get_hobby(hobbies, "tOm"))  # => "running"
    print(get_hobby(hobbies, "agO"))  # => "swimming"
