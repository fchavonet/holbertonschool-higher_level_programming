#!/usr/bin/python3

"""
Module with a function to check if an object is an instance of a class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance
    of the specified class or its subclasses.

    Parameters:
        obj: the object to check the class of.
        a_class: the class or tuple of classes to compare the object's type to.

    Returns:
        True if the object is an instance
        of the specified class or its subclasses,
        False otherwise.
    """
    return isinstance(obj, a_class)
