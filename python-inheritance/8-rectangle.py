#!/usr/bin/python3
"""
This module provides a simple definition for a
BaseGeometry class.

"""


class BaseGeometry:
    """BaseGeometry class."""


    def area(self):
        """Calculate area. Raises Exception
        if not implemented."""

        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ i dont fucking care """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ QUESO """


    def __init__(self, width, height):
        """ QUESOOOOOOOOOOOO """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
