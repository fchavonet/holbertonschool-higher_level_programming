def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first integer or float to be added.
        b (int or float): The second integer or float to be added.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
