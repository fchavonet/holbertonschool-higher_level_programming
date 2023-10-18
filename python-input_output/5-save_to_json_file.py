#!/usr/bin/python3

"""
This module contains a function that writes an Object
to a text file, using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes the provided Python object to a text file in JSON format.

    Args:
        my_obj: the Python object to be written to the file.
        filename (str): the name of the file
                        where the JSON representation will be saved.
    """

    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
