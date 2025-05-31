class CountedIterator:
    """
    An iterator that counts the number of items iterated over.
    """

    def __init__(self, iterable):
        """
        Initialize the iterator and set the counter to zero.

        Args:
            iterable (iterable): The iterable to be wrapped by CountedIterator.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """
        Fetch the next item from the iterator and increment the counter.

        Returns:
            The next item in the sequence.

        Raises:
            StopIteration: If there are no more items to iterate over.
        """
        item = next(self.iterator)
        self.counter += 1
        return item

    def get_count(self):
        """
        Get the current count of items iterated over.

        Returns:
            int: The number of items iterated over.
        """
        return self.counter
