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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size