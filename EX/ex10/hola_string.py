"""Hola string."""


def hola_string(count: int) -> str:
    """
    Make hola string.

    print(hola_string(3)) => "holaholahola"
    print(hola_string(0)) => ""

    :param count: number of times to repeat
    :return: The string "hola" repeated `count` times.
    """
    hola_count = ""
    while count > 0:
        hola_count += "hola"
        count -= 1
    return hola_count


if __name__ == '__main__':
    print(hola_string(3))
    print(hola_string(0))
