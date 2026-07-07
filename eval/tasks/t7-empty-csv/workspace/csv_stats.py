import csv


def stats(path):
    """Return (row_count, mean of the 'value' column) for a CSV file."""
    with open(path) as f:
        rows = list(csv.DictReader(f))
    total = sum(float(r["value"]) for r in rows)
    return len(rows), total / len(rows)
