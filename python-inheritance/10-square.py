#!/usr/bin/python3

"""
This module defines the `BaseGeometry` class and the `Square` class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Initializes a new Square instance.

    Attributes:
        __size (int): the size of the square.

    Methods:
        __init__(size): initializes a new Square
        instance with the specified size.
    """

    def __init__(self, size):
        """
        Initialize the new Square.

        Args:
            size (int): the size of the square.

        Raises:
            TypeError: if either size is not an integer.
            ValueError: if either size is less than or equal to 0.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: the area of the square.
        """
        return (self.__size * self.__size)
