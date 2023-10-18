#!/usr/bin/python3

"""
This module contains a function for writing a string to a text file
and return the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes the given string to a text file,
    and returns the number of characters written.

    Args:
        filename (str): the name of the file
                        to which the text will be written.
        text (str): the text to be written to the file.
    """

    with open(filename, 'w', encoding="utf-8") as file:
        return (file.write(text))
