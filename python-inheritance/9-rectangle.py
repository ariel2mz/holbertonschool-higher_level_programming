#!/usr/bin/python3
"""
This module provides a simple definition for the
BaseGeometry class and a Rectangle class that inherits from it.
"""


class BaseGeometry:
    """BaseGeometry class providing basic geometry functionalities."""

    def area(self):
        """Raises an Exception as area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a given value is an integer and greater than 0.

        Args:
            name (str): The name of the parameter (used in the error message).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance after validating its dimensions.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.
        Format: [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):

        def __init__(self, size):
        """
        Initializes a Rectangle instance after validating its dimensions.

        Args:
            size (int): The width of the rectangle.
        """
        self.integer_validator("size", size)
        self.__size = size