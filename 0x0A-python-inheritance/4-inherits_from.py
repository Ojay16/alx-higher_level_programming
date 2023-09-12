#!/usr/bin/python3
"""Defines an inherited class-checking function."""

def inherits_from(obj, a_class):
    """Checks if d object is a inherited instance of a class.
    Args:
        obj (any): The object checked.
        a_class (type): Class to match the type of obj to.
    Returns:
        If object is an inherited instance of a_class - return True.
        Otherwise - Returns False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
