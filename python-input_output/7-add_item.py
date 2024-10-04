#!/usr/bin/python3
"""
Script to add all command-line
arguments to a list and save it as JSON in a file.
"""


import sys
import os
import json


# Function to load an object from a JSON file
def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    :param filename: The name of the file containing the JSON data.
    :return: The object represented by the JSON data in the file.
    """


    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


# Function to save an object to a JSON file
def save_to_json_file(my_obj, filename):
    """
    Saves an object to a JSON file.

    :param my_obj: The object to be saved to the file.
    :param filename: The name of the file to save the object to.
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)


# Define the filename for storing the list
filename = "add_item.json"

# If the file exists, load the current list, otherwise create an empty list
if os.path.exists(filename):
    lista = load_from_json_file(filename)
else:
    lista = []

# Add command-line arguments to the list (excluding the script name)
lista.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(lista, filename)
