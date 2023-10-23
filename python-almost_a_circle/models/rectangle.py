#!/usr/bin/python3

"""
This module defines the `Base` class and the `Rectangle` class.
"""

from models.base import Base


class Rectangle(Base):
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

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

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
        Setter method to set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

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

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Getter method to retrieve the y-coordinate of the rectangle.

        Returns:
            int: the y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method to set the y-coordinate of the rectangle.

        Args:
            value (int): the y-coordinate of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: the area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints in `stdout` the Rectangle instance with the character `#`.
        """
        print("\n" * self.y, end="")
        for i in range(self.__height):
            print(" " * self.x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        Returns:
            str: a string representing the Rectangle instance in the format
            "([Rectangle] ({}) {}/{} - {}/{}"
             .format(self.id, self.x, self.y, self.width, self.height)).
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args):
        """
        Assigns an argument to each attribute.

        Args:
            *args: a variable number of arguments
            in the order (id, width, height, x, y).
        """
        if args:
            self.id, self.width, self.height, self.x, self.y = args[:5]
