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

    @staticmethod
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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file named after the class name.

        Args:
            cls (class): the class itself.
            list_objs (list of objects): a list of objects to
                                         be saved to a JSON file.
        """
        if list_objs is None:
            list_objs = []

        new_dictionary = []

        for object in list_objs:
            new_dictionary.append(object.to_dictionary())

        json_string = cls.to_json_string(new_dictionary)

        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as file:
            return (file.write(json_string))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON-formatted string to a list of dictionaries.

        Args:
            json_string (str): A JSON-formatted string to
                               be converted to a list of dictionaries.

        Returns:
            list: a list of dictionaries representing the objects' attributes.
                  Returns an empty list if the input is `None`.
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of the class from a dictionary of attributes.

        Args:
            cls (class): the class itself (`Rectangle` or `Square`).
            **dictionary (dict): Keyword arguments that represent the
                                 attributes of the object to be created.

        Returns:
            object: an instance of the class (`Rectangle` or `Square`) with
                    attributes specified in the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(4, 2)
        if cls.__name__ == "Square":
            dummy = cls(42)

        dummy.update(**dictionary)
        return dummy
