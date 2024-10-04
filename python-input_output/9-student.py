#!/usr/bin/python3
"""
Module that defines a Student class and provides a method to convert
the instance to a dictionary representation for JSON serialization.
"""


class Student:
    """
    Class that defines a student with first name, last name, and age.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        :param first_name: The student's first name.
        :param last_name: The student's last name.
        :param age: The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dictionary description with simple data structures
        (list, dictionary, string, integer, boolean)
        for JSON serialization of the Student instance.

        :return: A dictionary containing all serializable
        attributes of the Student object.
        """
        return self.__dict__

    def reload_from_json(self, json):
            """
            Replaces all attributes of the Student instance using the provided json.

            :param json: A dictionary with new attribute values to set on the instance.
            """
            for key, value in json.items():
                setattr(self, key, value)
