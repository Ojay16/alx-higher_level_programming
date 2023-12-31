#!/usr/bin/python3
"""defines square class."""

class Square:
    """Square class body."""

    def __init__(self, size=0):
        """Square contructor.
        Args:
            size (int): size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns  new area of the square."""
        return (self.__size * self.__size)
