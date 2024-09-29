#!/usr/bin/python3

from abc import ABC, abstractmethod

# Abstract class Animal
class Animal(ABC):
    """
    aaaa
    """

    @abstractmethod
    def sound(self):
        """
        aaasdasd
        """
        pass

# Subclass Dog implementing sound method
class Dog(Animal):
    """
    aaaaaaaaaaaaa
    """

    def sound(self):
        """
        aaaaaaa
        """
        return "Bark"

# Subclass Cat implementing sound method
class Cat(Animal):
    """
    aaaaa
    """

    def sound(self):
        """
        aaaaaa
        """
        return "Meow"
