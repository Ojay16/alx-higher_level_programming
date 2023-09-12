#!/usr/bin/python3
"""Defines class and inherited class-checking function."""

def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object checked.
        a_class (type): class to match the type of obj to.
    Returns:
        If obj is an instance or inherited inst of a_class - True.
        Otherwise -Return  False.
    """
    if isinstance(obj, a_class):
        return True
    return False
