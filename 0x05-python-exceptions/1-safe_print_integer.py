#!/usr/bin/python3

def safe_print_integer(value):

    """Printd an int with "{:d}".format().

    Args:
        value (int): The int to print.
    Returns:
        If  TypeError or ValueError occurs - False.
        else - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
