#!/usr/bin/python3

"""
This module defines the `BaseGeometry` class.
"""


class BaseGeometry:
    """
    This is the BaseGeometry class.

    Methods:
        area(self): raises an exception with a message
                    indicating that the method is not implemented.
    """
    def area(self):
        raise Exception("area() is not implemented")
