#!/usr/bin/python3
"""Defines an inherited list class MyList."""

class MyList(list):
    """Implements sorted printing for the list class."""

    def print_sorted(self):
        """Prints list in a sorted ascending order."""
        print(sorted(self))
