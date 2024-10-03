#!/usr/bin/python3
"""
adsda
"""


def append_write(filename="", text=""):
    """
    Appends the given text to the specified file
    and returns the number of characters added.

    :param filename: The name of the file to append to.
    :param text: The text to be appended to the file.
    :return: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        chars_written = file.write(text)
    return chars_written
