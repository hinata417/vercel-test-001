def purge_cutoff(now_ts, retention):
    """Return the timestamp before which records are purged.

    retention is the retention window in days.
    """
    return now_ts - retention * 60
