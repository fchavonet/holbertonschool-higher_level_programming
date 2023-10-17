#!/usr/bin/python3

"""
Module with a function to check if an object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    check if an object is an instance of a class
    that inherited (directly or indirectly) from the specified class

    Parameters:
    - obj: The object to check the class of.
    - a_class: The class to compare the object's type to.

    Returns:
    - True if the object is an instance of a class
    that inherits from the specified class,
    False otherwise.
    """
    return (isinstance(obj, a_class) and type(obj) is not a_class)
