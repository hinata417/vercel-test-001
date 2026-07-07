def normalize_phone(s):
    """Return digits only, e.g. '090-1234-5678' -> '09012345678'."""
    return s.replace("-", "")


def format_yen(n):
    return f"¥{n:,}"


def truncate(s, n):
    return s if len(s) <= n else s[: n - 1] + "…"
