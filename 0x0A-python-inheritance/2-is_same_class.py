#!/usr/bin/python3
"""Defines a class-checking function."""

def is_same_class(obj, a_class):
    """Checks if an object is an instance of a given class.

    Args:
        obj (any): The object checked.
        a_class (type): Class to match the type of obj to.
    Returns:
        If object is an instance of a_class - True.
        Otherwise - returnz False.
    """
    if type(obj) == a_class:
        return True
    return False
