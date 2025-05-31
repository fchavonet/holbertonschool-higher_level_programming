class Fish:
    """
    A class representing a fish.
    """

    def swim(self):
        """
        Print a message indicating that the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print a message indicating where the fish lives.
        """
        print("The fish lives in water")


class Bird:
    """
    A class representing a bird.
    """

    def fly(self):
        """
        Print a message indicating that the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print a message indicating where the bird lives.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish.
    """

    def swim(self):
        """
        Print a message indicating that the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Print a message indicating that the flying fish is soaring.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Print a message indicating where the flying fish lives.
        """
        print("The flying fish lives both in water and the sky!")
