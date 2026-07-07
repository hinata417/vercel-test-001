from parser import parse_price


def load_prices(strings):
    """Convert raw price strings into numbers."""
    return [int(parse_price(s)) for s in strings]
