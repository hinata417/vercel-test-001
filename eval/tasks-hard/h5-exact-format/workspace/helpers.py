def flatten(rows):
    return [x for row in rows for x in row]


def chunk(items, n):
    return [items[i:i + n] for i in range(0, len(items), n)]


def first(items, default=None):
    return items[0] if items else default
