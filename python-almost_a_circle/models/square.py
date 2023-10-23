#!/usr/bin/python3

"""
This module defines the `Rectangle` class and the `Square` class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is the Square class which is a specific type of rectangle
    where all sides are of equal length.

     Attributes:
        size (int): the length of each side of the square.
        x (int): the x-coordinate of the square (default is 0).
        y (int): the y-coordinate of the square (default is 0).
        id (int, optional): the unique identifier of
                            the square (default is None).
    Methods:
        __init__(self, size, x=0, y=0, id=None):
            Initializes a new Square instance.

        __str__(self):
            Returns a string representation of the Square instance.

    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Attributes:
            size (int): the length of each side of the square.
            x (int): the x-coordinate of the square (default is 0).
            y (int): the y-coordinate of the square (default is 0).
            id (int, optional): the unique identifier of
                                the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Return:
            str: a string representing the Square instance in the format
            "([Rectangle] ({}) {}/{} - {}"
             .format(self.id, self.x, self.y, self.width)).
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
