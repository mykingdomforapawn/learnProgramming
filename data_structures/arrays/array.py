""" Simple implementation of dynamic arrays. """

import ctypes


class Array:
    """ Array implemetation class. """

    def __init__(self):
        """ Init array object.

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

    def _make_array(self, array_capacity):
        """ Creates new array with input capacity.

        Parameters:
            array_capacity (int): Maximum array size

        Returns:
            [...] (cType): cType array to efficiently store homogenous data

        Raises:
            None

        """

        return (array_capacity * ctypes.py_object)()

    def list(self):
        """ List items of array as a string.

        Parameters:
            None

        Returns:
            [...] (str): Items of array with " " separator

        Raises:
            None

        """

        for _ in self.primary_array:
            return " ".join(str(self.primary_array[x]) for x in range(self.item_count))

    def __len__(self):
        """ Returns number of items in an array.

        Parameters:
            None

        Returns:
            [...] (int): Number of items in the array

        Raises:
            None

        """

        return self.item_count

    # TODO: size? oder ist das  das gleiche?

    # TODO: capacity?

    # TODO: is_empty()

    def __getitem__(self, item_index):
        """ Returns item at the given index.

        Parameters:
            item_index (int): Index to return the item

        Returns:
            [...] (cType): Item at the given index

        Raises:
            IndexError: If index is not in range of array

        """

        if not 0 <= item_index < self.item_count:
            return IndexError('index out of range!')
        return self.primary_array[item_index]

    # TODO: def setitem?

    def append(self, item):
        """ Add new item to array, increase capacity if not available.

        Parameters:
            item (int): Item to add to the end of the array

        Returns:
            None

        Raises:
            None

        """

        if self.item_count == self.array_capacity:
            self._enlarge_array(2 * self.array_capacity)

        self.primary_array[self.item_count] = item
        self.item_count += 1

    # TODO: prepend(item), append für 0

    # TODO: delte um hinten zu löschen

    # TODO: pop() letztes löschen und zurückgeben, mit delete_at z.b.

    def _enlarge_array(self, new_capacity):
        """ create array with input capacity and copy the contents of old to new array.

        Parameters:
            new_capacity (int): Increased capacity of the array

        Returns:
            None

        Raises:
            None

        """

        # TODO: change enlarge to resize, so that the array is ensmalled if too long (1/4)
        # when you reach capacity, resize to double the size
        # when popping an item, if size is 1/4 of capacity, resize to half

        secondary_array = self._make_array(new_capacity)
        for i in range(self.item_count):
            secondary_array[i] = self.primary_array[i]

        self.primary_array = secondary_array
        self.array_capacity = new_capacity

    def delete(self, item_index):
        """ Delete item at the given index.

        Parameters:
            item_index (int): Index to delete the item

        Returns:
            None

        Raises:
            None

        """

        if 0 > item_index or item_index > self.item_count - 1:
            return IndexError('index out of range!')

        while 0 <= item_index < self.item_count - 1:
            self.primary_array[item_index] = self.primary_array[item_index + 1]
            item_index += 1
        self.item_count -= 1

    # TODO: insert_at(index)
    # TODO: delete_at(index)

    # TODO: remove(item), rem index even if in multiple places
    # TODO: find(item) looks for value and returns first index with that value, -1 if not found


def main():
    print("hi")
    x = Array()

    x.append(10)
    x.append(20)
    # print(x.list())
    print(len(x))

    # x.delete(0)
    # x.list()

    # x.delete(7)


if __name__ == "__main__":
    main()
