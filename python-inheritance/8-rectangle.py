#!/usr/bin/python3

"""
This module defines the `BaseGeometry` class and the `Rectangle` class.
"""

# Import of the 7-base_geometry file.
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle:
    """
    Initializes a new Rectangle instance.

    Attributes:
        __width (int): the width of the rectangle.
        __height (int): the height of the rectangle.

    Methods:
        __init__(width, height): Initializes a new Rectangle
        instance with the specified width and height.
    """

    def __init__(self, width, height):
        """
        Initialize the new Rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is less than or equal to 0.
        """

        self.integer_validator("width", int)
        self.integer_validator("height", int)

        self.__width = width
        self.__height = height
