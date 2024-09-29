#!/usr/bin/python3

# Defining the custom VerboseList class
class VerboseList(list):
    """
    This class extends the built-in list and provides notification messages when items are added or removed.
    """

    # Override the append method
    def append(self, item):
        super().append(item)  # Call the original append method
        print(f"Added {item} to the list.")

    # Override the extend method
    def extend(self, iterable):
        num_items = len(iterable)
        super().extend(iterable)  # Call the original extend method
        print(f"Extended the list with {num_items} items.")

    # Override the remove method
    def remove(self, item):
        print(f"Removed {item} from the list.")  # Print before removing
        super().remove(item)  # Call the original remove method

    # Override the pop method
    def pop(self, index=None):
        # If no index is specified, pop the last item
        if index is None:
            popped_item = super().pop()  # Pop the last item
            print(f"Popped {popped_item} from the list.")
            return popped_item
        else:
            popped_item = super().pop(index)  # Pop the item at the specified index
            print(f"Popped {popped_item} from index {index} of the list.")
            return popped_item


