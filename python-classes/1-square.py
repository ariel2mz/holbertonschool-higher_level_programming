#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
Class that defines a square with a private instance attribute 'size'.

    Attributes:
        __size (int): The size of the square.
    """__size (int)

    def __init__(self, size):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
