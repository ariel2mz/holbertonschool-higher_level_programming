#!/usr/bin/python3
"""
This module provides a simple definition for a Rectangle class.

The Rectangle , with no attributes or methods. It serves as a
basic strucrelated to square functionality.
"""


class Rectangle:
    """
    Easdas Asddsa asdsasad

    DASDsa
    """
    def __init__(self, width=0, height=0):
        """
        sadasdsad
        
        asdasdas
        """
        self.width = width
        self.height = height
    @property
    def width(self):
        """
        asadsadsa
        sadsadsa
        """
        return self.width
    @width.setter
    def width(self, value):
        """
        sadsadsadsa

        sadsadsa
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
    @property
    def height(self):
        """
        asadsadsa
        sadsadsa
        """
        return self.width
    @height.setter
    def height(self, value):
        """
        sadsadsadsa

        sadsadsa
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")