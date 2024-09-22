#!/usr/bin/python3
"""
This module provides a definition for the Rectangle class.

The Rectangle class represents a basic geometric shape, providing
attributes to manage its width and height, as well as setter and
getter methods to validate input.
"""


class Rectangle:
    """
    Class that defines a rectangle with private instance attributes
    for width and height, including input validation.

    Attributes:
        __width (int): The width of the rectangle
        (must be a non-negative integer).
        __height (int): The height of the rectangle
        (must be a non-negative integer).
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle instance with optional width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is less than 0.
        """
        self.width = width  # Calls the width setter for validation
        self.height = height  # Calls the height setter for validation

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute, with validation.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute, with validation.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Returns the area.

            Args:
                self (Rectangle): the rectangle
            """
        return self.__height * self.__width

    def perimeter(self):
        """
            Returns the perimeter.

            Args:
                self (Rectangle): the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return self.__height + self.__width

