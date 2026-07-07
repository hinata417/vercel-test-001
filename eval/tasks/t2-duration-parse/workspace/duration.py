def parse_duration(s):
    """Parse a duration like '2h', '45m' or '1h30m' into total minutes."""
    total = 0
    num = ""
    for ch in s:
        if ch.isdigit():
            num += ch
        elif ch == "h":
            total += int(num) * 60
        elif ch == "m":
            total += int(num)
    return total
