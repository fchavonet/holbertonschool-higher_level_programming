#!/usr/bin/python3

"""
This module contains a function that returns the dictionary description
with simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Converts a Python object to a dictionary.

    Args:
        obj (object): the Python object to be converted to a dictionary.

    Returns:
        dict: a dictionary representation of the
        Python object for JSON serialization.
    """

    return obj.__dict__
