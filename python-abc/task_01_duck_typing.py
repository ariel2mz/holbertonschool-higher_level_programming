#!/usr/bin/python3

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
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Rectangle class inheriting from Shape
class Rectangle(Shape):
    """
    Class representing a rectangle. Requires width and height as input.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Function to print area and perimeter
def shape_info(shape):
    """
    Function that prints the area and perimeter of the shape passed to it.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
