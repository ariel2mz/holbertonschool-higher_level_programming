#!/usr/bin/python3
"""
QUESOOOO
"""


import json


def save_to_json_file(my_obj, filename):
    """
    asdsadsa
    """

    with open(filename, "w") as file:
        return file.write(json.dumps(my_obj))
