#!/usr/bin/python3
class Car():
    
    def __init__(self, brand, model, year):

        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"{self.year}\n")
        print(f"{self.brand}\n")
        print(f"{self.model}")

auto1 = Car("Quesobus", "Parmesano", 2005)
Car.display_info(auto1)
