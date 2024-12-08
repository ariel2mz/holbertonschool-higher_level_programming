#!/usr/bin/python3
class Person():
    species = "Homo sapiens"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def specie(cls, specie):
        cls.specie = specie

    def printinfo(self):
        print(f"{self.name}")
        print(f"{self.age}")
        print(f"{self.species}")

juani = Person("juani", 20)
Person.printinfo(juani)
