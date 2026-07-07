def parse_bool(s):
    """Parse a human-entered boolean flag.

    Truthy inputs (case-insensitive): 'true', '1', 'yes', 'on'.
    Everything else is False.
    """
    return s == "true"
