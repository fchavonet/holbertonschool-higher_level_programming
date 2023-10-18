#!/usr/bin/python3

"""
This module contains a function that appends a string at the end of
a text file and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends the given string to the end of a text file
    and returns the number of characters added.

    Args:
        filename (str): the name of the file
                        to which the text will be appended.
        text (str): the text to be appended to the file.
    """

    with open(filename, 'a', encoding="utf-8") as file:
        return (file.write(text))
