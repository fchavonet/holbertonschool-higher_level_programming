#!/usr/bin/python3

"""
This module contains a function for reading
and printing the contents of a file.
"""


def read_file(filename=""):
    """
    Read and print the contents of a file.

    Args:
        filename (str): the name of the file to read.
    """

    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
