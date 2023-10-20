#!/usr/bin/python3

"""
This module contains a function that returns a list of lists
of integer representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Generate the first 'n' rows of Pascal's Triangle.

    Args:
        n (int): the number of rows to generate in the Pascal's Triangle.

    Returns:
        list: a list of lists of integer representing
              the Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    pascal_triangle = [[1]]

    for row_number in range(1, n):
        new_row = [1]
        previous_row = pascal_triangle[-1]

        for i in range(len(previous_row) - 1):
            new_value = previous_row[i] + previous_row[i + 1]
            new_row.append(new_value)

        if n >= 2:
            new_row.append(1)

        pascal_triangle.append(new_row)

    return pascal_triangle
