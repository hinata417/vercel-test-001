from helpers import first


def get_user(users, name):
    return first([u for u in users if u.name == name])


def count_orders(orders):
    return len(orders)


def health():
    return "ok"
