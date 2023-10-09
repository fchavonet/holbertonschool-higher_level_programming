#!/usr/bin/python3

"""
This script defines a "Square" class to represent a square.
"""


class Square:
    """
    Square class with a private instance attribute: size.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
