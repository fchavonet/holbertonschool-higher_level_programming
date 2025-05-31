class SwimMixin:
    """
    Mixin to add swimming functionality.
    """

    def swim(self):
        """
        Print a message indicating that the creature swims.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin to add flying functionality.
    """

    def fly(self):
        """
        Print a message indicating that the creature flies.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class representing a dragon with swimming and flying abilities.
    """

    def roar(self):
        """
        Print a message indicating that the dragon roars.
        """
        print("The dragon roars!")
