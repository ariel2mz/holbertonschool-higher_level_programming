#!/usr/bin/python3
"""
This module defines a Rectangle class.

The Rectangle class models a rectangle with attributes for width and height,
and provides methods for calculating the area, perimeter, and string
representation of the rectangle.
"""


class Rectangle:
    """
    A class to represent a rectangle with width and height.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle object.

        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def set_print_symbol(cls, symbol):
        """
        Change the symbol used for printing the rectangle.

        Args:
            symbol (Any): The symbol to use for printing.
        """
        cls.print_symbol = symbol

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string representation of the rectangle using `#`.

        Each line represents a row, and each `#` represents a unit of width.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) 
                          * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Return a string representation of the rectangle for recreation.

        Returns:
            str: A string that can recreate the rectangle using `eval`.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Return adsadsadsa

        asdsadsads
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
