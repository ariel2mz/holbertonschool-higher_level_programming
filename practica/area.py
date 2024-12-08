#!/usr/bin/python3
class Shape:
    
    def area(self):
        raise  NotImplementedError
    
class Circle(Shape):
    
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        print({self.radio * 3})

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        print({self.width * self.height})


circulito = Circle(5)
rectangulopolis = Rectangle(2, 4)
Circle.area(circulito)
Rectangle.area(rectangulopolis)