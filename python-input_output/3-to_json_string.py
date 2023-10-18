#!/usr/bin/python3

"""
This module contains a function that returns the JSON
representation of an object (string).
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of the provided object as a string.

    Args:
        my_obj: the object to be converted to a JSON string.

    Returns:
        str: the JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
