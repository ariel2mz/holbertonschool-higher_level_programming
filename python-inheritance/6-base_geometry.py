#!/usr/bin/python3
"""
This module provides a simple definition for a BaseGeometry class.

"""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Calculate area. Raises Exception if not implemented."""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ i dont fucking care """
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
