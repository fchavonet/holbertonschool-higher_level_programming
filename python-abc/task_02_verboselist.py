class VerboseList(list):
    """
    Custom list class that prints notifications when items are added or removed.
    """

    def append(self, item):
        """
        Add an item to the list and print a message.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """
        Extend the list with multiple items and print a message.
        """
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """
        Remove an item from the list and print a message.
        If the item is not found, print a warning.
        """
        if item in self:
            print(f"Removed [{item}] from the list.")
            super().remove(item)
        else:
            print(f"Item [{item}] not found in the list.")

    def pop(self, index=-1):
        """
        Remove and return an item from the list at the given index.
        Print a message before removing the item.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
