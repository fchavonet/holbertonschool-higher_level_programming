#!/usr/bin/python3

"""
This module defines a `Rectangle` class to represent a square.
"""


class Rectangle:
    """
    The `Rectangle` class is used to represent a rectangle.

    Attributes:
        number_of_instances (int): Class-level variable to keep track of
                                   the number of Rectangle instances created.

    Args:
            width (int): The width of the rectangle.
                         Default is 0.
            height (int): The height of the rectangle.
                          Default is 0.

    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
                         Default is 0.
            height (int): The height of the rectangle.
                          Default is 0.
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method to retrieve the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """

        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter method to set the width of the rectangle.

        Args:
            value (int): The width of the rectangle.
                         It must be a non-negative integer.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """

        if type(value) is not (int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method to retrieve the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """

        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter method to set the height of the rectangle.

        Args:
            value (int): The height of the rectangle.
                         It must be a non-negative integer.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """

        if type(value) is not (int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The area of the rectangle.
        """

        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width + self.__height) * 2)

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """

        return (self.__width * self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle with `#`.

        Returns:
            str: A string representing the rectangle.
        """

        string = ""

        if self.__height != 0 and self.__width != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    string += "#"
                if i < self.__height - 1:
                    string += "\n"

        return (string)

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        in the format "Rectangle(width, height)".

        Returns:
        str: A string representation of the rectangle object.
        """

        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        Print the message `Bye rectangle...`
        when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
