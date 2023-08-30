#!/usr/bin/python3
# 2-square.py
"""defines Square class."""

class Square:
    """ body of Square class"""

    def __init__(self, size=0):
        """Square class
        Args:
            size (int): size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
