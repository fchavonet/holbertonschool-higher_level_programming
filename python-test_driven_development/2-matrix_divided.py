#!/usr/bin/python3

"""
Module with a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor (`div`).

    Args:
        matrix (list of lists): List of lists containing integers or floats.
        div (int or float): Divisor used to divide each element of the matrix.

    Returns:
        list of lists: New matrix containing all divided elements.
                       The result is rounded to two decimal places.

    Raises:
        ZeroDivisionError: If `div` is zero, division by zero is not allowed.
        TypeError: If `div` is not a number (int or float).
                   "If matrix is not a valid matrix or is empty."
                   If any row of the matrix is not a list or is empty,
                   If the rows in the matrix have different sizes.
    """

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if type(matrix) is not list or matrix == []:
        raise TypeError(error_msg)

    new_matrix = []

    for row in matrix:
        if type(row) is not (list) or row == []:
            raise TypeError(error_msg)
        elif len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []

        for number in row:
            if type(number) not in (int, float):
                raise TypeError(error_msg)
            new_row.append(round(number / div, 2))
        new_matrix.append(new_row)

    return new_matrix
