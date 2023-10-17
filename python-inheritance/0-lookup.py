#!/usr/bin/python3

"""
This module defines a function called "lookup" that takes an object
as an argument and provides a list of its attributes and methods.
"""


def lookup(obj):
    """
    Takes an object and provides a list of its attributes and methods.

    Args:
        obj: the object for which you want to retrieve attributes and methods.

    Returns:
        A list of strings representing what you want to retrieve.
    """
    return dir(obj)
