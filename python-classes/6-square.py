#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Class that defines a square with private 
    instance attributes 'size' and 'position'.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): 
        Initializes the square with a given size and position.
        area(self): Returns the current area of the square.
        my_print(self): Prints the square using '#' character.
        size(self): Retrieves the size.
        size(self, value): Sets the size with validation.
        position(self): Retrieves the position.
        position(self, value): Sets the position with validation.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a given size and position.

        Args:
            size (int, optional):
            The size of the square (default is 0).
            position (tuple, optional):
            The position of the square (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character. 
        If size is 0, prints an empty line.
        The position is respected by adding spaces before each line.
        """
        if self.__size == 0:
            print("")
            return

        # Print new lines for vertical positioning (position[1])
        for _ in range(self.__position[1]):
            print("")

        # Print the square with spaces according to horizontal position (position[0])
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
