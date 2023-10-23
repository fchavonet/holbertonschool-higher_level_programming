#!/usr/bin/python3

"""
This module defines the `Base` class and the `Rectangle` class.
"""

from models.base import Base


class Rectangle:
    """
    This is the Rectangle class to represent a rectangle.

    Attributes:
        width (int): the width of the rectangle.
        height (int): the height of the rectangle.
        x (int): the x-coordinate of the rectangle (default is 0).
            y (int): the y-coordinate of the rectangle (default is 0).
        id (int, optional): the unique identifier of
                                the rectangle (default is None).

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Initializes a new Rectangle instance.

        width(self):
            Getter method to retrieve the width of the rectangle.

        width(self, value):
            Setter method to set the width of the rectangle.

        height(self):
            Getter method to retrieve the height of the rectangle.

        height(self, value):
            Setter method to set the height of the rectangle.

        x(self):
            Getter method to retrieve the x-coordinate of the rectangle.

        x(self, value):
            Setter method to set the x-coordinate of the rectangle.

        y(self):
            Getter method to retrieve the y-coordinate of the rectangle.

        y(self, value):
            Setter method to set the y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
            x (int): the x-coordinate of the rectangle (default is 0).
            y (int): the y-coordinate of the rectangle (default is 0).
            id (int, optional): the unique identifier of
                                the rectangle (default is None).
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter method to retrieve the width of the rectangle.

        Returns:
            int: the width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method to set the width of the rectangle.

        Args:
            value (int): the width of the rectangle.
        """

        self.__width = value

    @property
    def height(self):
        """
        Getter method to retrieve the height of the rectangle.

        Returns:
            int: the height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Getter method to retrieve the x-coordinate of the rectangle.

        Returns:
            int: the x-coordinate of the rectangle.
        """

        self.__height = value

    @property
    def x(self):
        """
        Getter method to retrieve the x-coordinate of the rectangle.

        Returns:
            int: the x-coordinate of the rectangle.
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method to set the x-coordinate of the rectangle.

        Args:
            value (int): the x-coordinate of the rectangle.
        """

        self.__x = value

    @property
    def y(self):
        """
        Getter method to retrieve the y-coordinate of the rectangle.

        Returns:
            int: the y-coordinate of the rectangle.
        """

        return self.__y

    @x.setter
    def y(self, value):
        """
        Setter method to set the y-coordinate of the rectangle.

        Args:
            value (int): the y-coordinate of the rectangle.
        """

        self.__y = value
