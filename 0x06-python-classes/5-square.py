#!/usr/bin/python3
"""sqaure class defination"""


class Square:
    """class body"""

    def __init__(self, size):
        """Square contructor
        Args:
            size (int): size of new square.
        """
        self.size = size

    @property
    def size(self):
        """setter and getter for __size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints stdout of the square with the character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
