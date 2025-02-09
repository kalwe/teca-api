from datetime import datetime, timezone


def aware_utcnow():
    """
    Get the current time in UTC with timezone awareness.

    Returns:
        datetime: The current UTC time with timezone information.
    """
    return datetime.now(timezone.utc)


def aware_now(format: str = "%Y-%m-%d") -> str:
    return datetime.now().strftime(format)


def aware_utcfromtimestamp(timestamp):
    """
    Convert a UNIX timestamp to a timezone-aware UTC datetime.

    Args:
        timestamp (float): The UNIX timestamp to convert.

    Returns:
        datetime: A timezone-aware UTC datetime representation of the timestamp.
    """
    return datetime.fromtimestamp(timestamp, timezone.utc)


def naive_utcnow():
    """
    Get the current time in UTC as a naive datetime (without timezone information).

    Returns:
        datetime: The current UTC time as a naive datetime.
    """
    return aware_utcnow().replace(tzinfo=None)


def naive_utcfromtimestamp(timestamp):
    """
    Convert a UNIX timestamp to a naive UTC datetime (without timezone information).

    Args:
        timestamp (float): The UNIX timestamp to convert.

    Returns:
        datetime: A naive UTC datetime representation of the timestamp.
    """
    return aware_utcfromtimestamp(timestamp).replace(tzinfo=None)
