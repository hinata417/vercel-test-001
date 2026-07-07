from loader import load_prices


def total_order(strings):
    """Total an order given raw price strings."""
    return round(sum(load_prices(strings)), 2)
