from config import MAX_ITEMS


def validate_cart(items):
    if len(items) > MAX_ITEMS:
        raise ValueError("cart may hold at most 10 items")
    return True
