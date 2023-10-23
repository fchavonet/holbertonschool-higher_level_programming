#!/usr/bin/python3

"""
This module defines the `Rectangle` class and the `Square` class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is the `Square` class, which is a specific type of rectangle
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

        update(self, *args, **kwargs):
            Assigns arguments to each attribute.

        Args:
            *args: a variable number of arguments.
                The order is important:
                    1st argument should be the `id` attribute
                    2nd argument should be the `size` attribute
                    3rd argument should be the `x` attribute
                    4th argument should be the `y` attribute
            **kwargs: a variable number of keyword arguments.
                These allow you to update attributes by name.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Args:
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
            raise TypeError("size must be an integer")

        if value <= 0:
            raise ValueError("size must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: A string representing the Square instance in the format
            "[Square] ({}) {}/{} - {}"
            .format(self.id, self.x, self.y, self.size).
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """
        Assigns arguments to each attribute.

        Args:
            *args: a variable number of arguments.
                The order is important:
                    1st argument should be the `id` attribute
                    2nd argument should be the `size` attribute
                    3rd argument should be the `x` attribute
                    4th argument should be the `y` attribute
            **kwargs: a variable number of keyword arguments.
                These allow you to update attributes by name.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
