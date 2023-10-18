#!/usr/bin/python3

"""
This module contains a function
that creates an Object from a “JSON file”.
"""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): the name of the JSON file
                        from which to load the object.

    Returns:
        object: the Python object created from the JSON file.
    """

    with open(filename) as file:
        return json.load(file)
