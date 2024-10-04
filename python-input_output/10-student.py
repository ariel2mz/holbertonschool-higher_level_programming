#!/usr/bin/python3
"""
Module that defines a Student class with serialization and
deserialization mechanisms.
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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes contained in this
        list will be retrieved. Otherwise, all attributes are retrieved.

        :param attrs: A list of attribute names to retrieve (optional).
        :return: A dictionary representing the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {
                key: value for key, value in self.__dict__.items()
                if key in attrs
            }

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from
        a dictionary.

        :param json: A dictionary with new attribute values.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
