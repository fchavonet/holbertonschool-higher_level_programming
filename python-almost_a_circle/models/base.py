#!/usr/bin/python3

"""
Module that defines a base class named `Base` that manages
unique identifiers for its instances.
"""

import json


class Base:
    """
    This is the Base class, which will serve as the foundation for all other
    classes in the project. It manages the `id` attribute, ensuring that each
    instance has a unique identifier.

    Attributes:
        __nb_objects (int): a private class attribute that keeps
        track of the number of Base objects created.
        id (int): a public instance attribute representing the
        unique identifier of the instance.

    Methods:
        __init__(self, id=None):
            Initializes a new Base instance.
            If `id` is provided, it is assigned to the 'id' attribute.
            If `id` is not provided, it is automatically
            generated based on '__nb_objects'.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance.

        Args:
            id (int, optional): an integer representing the desired `id` value.
                                If 'id' is provided, it is assigned to
                                the 'id' attribute.
                                If 'id' is not provided, it is automatically
                                generated based on '__nb_objects'.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list of dict): a list of dictionaries
                                              to be converted
                                              to a JSON string.

        Returns:
            str: A JSON-formatted string representing the list of dictionaries.
                Returns an empty list if the input is `None`.
        """
        if list_dictionaries is None:
            return []
        else:
            return (json.dumps(list_dictionaries))
