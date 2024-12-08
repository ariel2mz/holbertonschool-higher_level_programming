#!/usr/bin/python3
class Animal:
    def __init__(self, name, specie):
        self.name = name
        self.specia = specie

    def make_sound(self):
        print("AAAAAAAAA")

class Perro(Animal):
    def make_sound(self):
        print("soy un perrovich anashe")


animal = Animal("animalopolis", "quesobus")
Animal.make_sound(animal)
perro = Perro("Perroide", "perroide")
Perro.make_sound(perro)
print("\n")

Perro.make_sound(animal)
Animal.make_sound(perro)
