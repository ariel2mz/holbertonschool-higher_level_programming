#!/usr/bin/python3
"""
QUESOOOO
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    :param filename: The name of the file containing the JSON data.
    :return: The object represented by the JSON data in the file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
