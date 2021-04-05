"""Implementation of a stack based on a dynamic array. """

import ctypes


class ArrayStack:
    """Stack implemetation class. """

    def __init__(self):
        """Init stack object as an array.

        Parameters:
            None

        Returns:
            None

        Raises:
            None
        """
        self.item_count = 0
        self.array_capacity = 1
        self.primary_array = self._make_array(self.array_capacity)

    def __getitem__(self, index):
        """Returns item at the given index.

        Parameters:
            index (int): Index to return the item

        Returns:
            [...] (cType): Item at the given index

        Raises:
            IndexError: If index is not in range of underlying array
        """
        if not 0 <= index < self.item_count:
            return IndexError('index out of range!')
        return self.primary_array[index]

    def _make_array(self, array_capacity):
        """Creates new array with input capacity.

        Parameters:
            array_capacity (int): Maximum array size

        Returns:
            [...] (cType): cType array to efficiently store homogenous data

        Raises:
            None
        """
        return (array_capacity * ctypes.py_object)()

    def _resize(self, new_capacity):
        """Create array with input capacity and copy the contents of old to new array.

        Parameters:
            new_capacity (int): Increased capacity of the array

        Returns:
            None

        Raises:
            None
        """
        secondary_array = self._make_array(new_capacity)
        for i in range(self.item_count):
            secondary_array[i] = self.primary_array[i]

        self.primary_array = secondary_array
        self.array_capacity = new_capacity

    def list(self):
        """List items of array as a string.

        Parameters:
            None

        Returns:
            [...] (str): Items of array with " " separator

        Raises:
            None
        """
        if not self.is_empty():
            for _ in self.primary_array:
                return " ".join(str(self.primary_array[x]) for x in range(self.item_count))

    def size(self):
        """Returns number of items in the stack.

        Parameters:
            None

        Returns:
            [...] (int): Number of items in the array

        Raises:
            None
        """
        return self.item_count

    def is_empty(self):
        """Returns True if the array is empty.
        Parameters:
            None

        Returns:
            [...] (bool): Indicator if array is empty

        Raises:
            None
        """
        if self.item_count == 0:
            return True
        else:
            return False

    def push(self, item):
        """Add new item to the end of the array, increase capacity if not available.

        Parameters:
            item (int): Item to add at the index

        Returns:
            None

        Raises:
            None
        """
        if self.item_count == self.array_capacity:
            self._resize(2 * self.array_capacity)

        self.primary_array[self.item_count] = item
        self.item_count += 1

    def top(self):
        pass

    def pop(self):
        """Delete and return the last item of the array, decrease capacity if possible.

        Parameters:
            None

        Returns:
            pop_item (int): Item that now is deleted from the array

        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            return IndexError('the stack is empty!')

        pop_item = self.primary_array[self.item_count - 1]
        self.item_count -= 1

        if self.item_count == self.array_capacity // 4:
            self._resize(self.array_capacity // 2)

        return pop_item


def main():

    print("Init and push items to stack.")
    x = ArrayStack()
    x.push(10)
    x.push(20)
    print("Stack:", x.list(), ", Size:", x.size())

    print("Check if array is empty.")
    print(x.is_empty())
    print("Stack:", x.list(), ", Size:", x.size())

    print("Pop items from stack.")
    print(x.pop())
    print(x.pop())
    print(x.pop())

    print("Stack:", x.list(), ", Size:", x.size())


if __name__ == "__main__":
    main()
