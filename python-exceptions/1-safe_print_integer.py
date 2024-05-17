#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints an integer using "{:d}".format().

    Args:
    value: The value to print, which can be any type.

    Returns:
    bool: True if value was an integer and printed correctly, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
