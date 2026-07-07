def overlaps(a, b):
    """Return True if half-open intervals a and b overlap.

    Intervals are (start, end) tuples; end is exclusive.
    """
    return a[0] <= b[1] and b[0] <= a[1]
