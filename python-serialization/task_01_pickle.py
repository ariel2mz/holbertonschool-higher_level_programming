import json
import pickle

class CustomObject:
    # Constructor method (optional)
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    # Example method
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {True}")
    
    def serialize(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)
    
    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except EOFError:
            print(f"Error: File '{filename}' is empty or corrupted.")
        except pickle.UnpicklingError:
            print(f"Error: File '{filename}' contains invalid serialized data.")
        return None