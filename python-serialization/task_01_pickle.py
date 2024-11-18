import json
import pickle

class CustomObject:
    # Constructor method (optional)
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.student = is_student

    # Example method
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {True}")
    
    def serialize(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)
    
    @classmethod
    def deserialize(cls, filename):
         with open(filename, "rb") as file:
            return pickle.load(file)
