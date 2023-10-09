#!/usr/bin/python3

"""
This script defines a "Square" class to represent a square.
"""


class Square:
    """
    This is the Square class with a private instance attribute: __size.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
                It must be a non-negative integer.
        """
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = size
