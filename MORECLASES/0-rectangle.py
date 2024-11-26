#!/usr/bin/python3
"""
This module provides a simple definition for a Rectangle class.

The Rectangle , with no attributes or methods. It serves as a
basic strucrelated to square functionality.
"""


class Rectangle:
    """
Class that defines a square with a private instance attribute 'size'.

    Attributes:
        __height (int): The width of the rectangle.
        __heigth (int): The height of the rectangle.
    """
    __width (int)
    __heigth (int)


def width(self):
    return self.__width

def width(self, value):
    if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

def height(self):
    return self.__height

def height(self, value):
    if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

def __init__(self, width=0, height=0):
    self.__width = width
    self.__height = height
