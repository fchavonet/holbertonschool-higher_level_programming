from abc import ABC, abstractmethod

"""
This module defines an abstract class Animal and two subclasses, Dog and Cat.
"""


class Animal(ABC):
    """
    Abstract class representing an animal.

    Requires subclasses to implement the sound() method.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.

        Returns:
            str: the sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Represents a dog, inheriting from Animal.

    Implements the sound() method for a dog.
    """

    def sound(self):
        """
        Returns the sound a dog makes.

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Represents a cat, inheriting from Animal.

    Implements the sound() method for a cat.
    """

    def sound(self):
        """
        Returns the sound a cat makes.

        Returns:
            str: "Meow"
        """
        return "Meow"
