#!/usr/bin/python3

"""
Module with a function to check if an object is an instance of a class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of the specified class.

    Parameters:
        obj: the object to check the class of.
        a_class: the class to compare the object's type to.

    Returns:
        `True` if the object is an exact instance of the specified class,
        `False` otherwise.
    """
    return (type(obj) is a_class)
