"""Make hola string."""


def hola_string(count: int) -> str:
    """
    Make hola string.

    print(hola_string(3)) => "holaholahola"
    print(hola_string(0)) => ""

    :param count: number of times to repeat
    :return: The string "hola" repeated `count` times.
    """
    holas = ""
    for i in range(count):
        holas += "hola"
    return holas


if __name__ == '__main__':
    print(hola_string(3))
    print(hola_string(0))
