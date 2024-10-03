#!/usr/bin/python3
"""
adssada
"""


def write_file(filename="", text=""):
    """
    Writes the given text to the specified file.

    :param filename: The name of the file to write to.
    :param text: The text to be written to the file.
    :return: None
    """
    with open(filename, "r") as file:
        with open(filename, "w") as write:
            write.write(file.read() + text)