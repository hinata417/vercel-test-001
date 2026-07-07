class User:
    def __init__(self, name):
        self.name = name


class Order:
    def __init__(self, items):
        self.items = items


def new_user(name):
    return User(name)
