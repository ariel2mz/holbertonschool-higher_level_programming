#!/usr/bin/python3
"""
sadsadsad
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures
    (list, dictionary, string, integer, boolean)
    for JSON serialization of an object.

    :param obj: The instance of a class to be serialized.
    :return: A dictionary containing all serializable attributes of the object.
    """
    return obj.__dict__
