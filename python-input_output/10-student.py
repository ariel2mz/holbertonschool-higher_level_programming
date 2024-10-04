#!/usr/bin/python3
"""
A class that defines a student with methods for JSON serialization
and deserialization.
"""

class Student:
    """
    A class that defines a student by first name, last name, and age.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        :param first_name: The student's first name.
        :param last_name: The student's last name.
        :param age: The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        :param attrs: A list of attribute names to include in the dictionary.
                      If attrs is a list of strings, only those attributes
                      are retrieved. Otherwise, all attributes are retrieved.
        :return: A dictionary representation of the instance.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            # Only retrieve the attributes listed in attrs
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        else:
            # Retrieve all attributes
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using the provided json.

        :param json: A dictionary with new attribute values to set on the instance.
        """
        for key, value in json.items():
            setattr(self, key, value)
