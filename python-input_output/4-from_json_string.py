#!/usr/bin/python3

"""
This module contains a function returns an object
(Python data structure) represented by a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Returns a Python object represented by the provided JSON string.

    Args:
        my_str (str): the JSON string to be converted into a Python object.

    Returns:
        object: the Python data structure represented by the JSON string.
    """

    return (json.loads(my_str))
