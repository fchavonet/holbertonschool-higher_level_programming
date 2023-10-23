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

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square's sides.

        Returns:
            int: the size of the square's sides.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square's sides.

        Args:
            value (int): the size of the square's sides.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

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
