#!/usr/bin/python3

"""
Module with a function that prints a square with the character `#`.
"""


def print_square(size):
    """
    Print a square with the character `#`.

    Args:
        size (int): The side length of the square (psitive integer).

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is a negative integer.
    """

    if type(size) is not (int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for row in range(0, size):
        for column in range(0, size):
            print("#", end="")
        print()
