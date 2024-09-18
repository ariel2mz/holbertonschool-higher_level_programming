#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Class that defines a square with a private instance attribute 'size'.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes the square with a given size.
        area(self): Returns the current area of the square.
        size(self): Retrieves the size.
        size(self, value): Sets the size with validation.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Using the property setter for validation

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2