"""Capitalize first letter of a string."""


def capitalize_first_letter(string_with_low: str) -> str:
    """Return the same string with the first letter capitalized."""
    # Take the letter at the first index and capitalize it and then add the rest of the string from index 1 going forward.
    return string_with_low.capitalize()[0:1] + string_with_low[1:]


if __name__ == '__main__':
    print(capitalize_first_letter('heLLO'))
