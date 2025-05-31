from abc import ABC, abstractmethod
import math

"""
This module defines an abstract Shape class with area and perimeter methods.
It includes Circle and Rectangle subclasses,
and a shape_info function to display their properties.
"""


class Shape(ABC):
    """
    Abstract class representing a shape.

    Requires subclasses to implement area() and perimeter() methods.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.

        Returns:
            float: the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.

        Returns:
            float: the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Represents a circle, inheriting from Shape.

    Attributes:
        radius (float): the radius of the circle.
    """

    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle, inheriting from Shape.

    Attributes:
        width (float): the width of the rectangle.
        height (float): the height of the rectangle.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.

    Args:
        shape (Shape): an object implementing area and perimeter methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
