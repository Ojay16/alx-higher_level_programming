#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""

class BaseGeometry:
    """Reps base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates d parameter as an integer.
        Args:
            name (str): name of parameter.
            value (int): parameter to be validated.
        Raises:
            TypeError: If value is not an int.
            ValueError: If value is <= zero.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
