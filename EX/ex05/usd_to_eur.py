"""USD to EUR."""


def usd_to_eur(usd: int):
    """Return USD converted to EUR at rate 1USD = 0.8EUR."""
    return usd * 0.8


if __name__ == '__main__':
    usd = float(input('Enter USD: '))
    print(usd_to_eur(usd))
