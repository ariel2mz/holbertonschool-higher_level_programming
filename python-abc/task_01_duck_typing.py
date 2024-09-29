#!/usr/bin/python3

import math
from abc import ABC, abstractmethod

# Abstract class Shape
class Shape(ABC):
    """
    Abstract class that defines two abstract methods: area and perimeter.
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Circle class inheriting from Shape
class Circle(Shape):
    """
    Class representing a circle. Requires radius as input.
    """

    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius
