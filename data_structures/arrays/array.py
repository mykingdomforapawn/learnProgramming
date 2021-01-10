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

    def __getitem__(self, index):
        """ Returns item at the given index.

        Parameters:
            index (int): Index to return the item

        Returns:
            [...] (cType): Item at the given index

        Raises:
            IndexError: If index is not in range of array

        """
        if not 0 <= index < self.item_count:
            return IndexError('index out of range!')
        return self.primary_array[index]

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

    def _resize(self, new_capacity):
        """ Create array with input capacity and copy the contents of old to new array.

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

    def size(self):
        """ Returns number of items in an array.

        Parameters:
            None

        Returns:
            [...] (int): Number of items in the array

        Raises:
            None

        """

        return self.item_count

    def capacity(self):
        """ Returns maximum number of items in an array.

        Parameters:
            None

        Returns:
            [...] (int): Maximum number of items in the array

        Raises:
            None

        """

        return self.array_capacity

    def is_empty(self):
        """ Returns True if the array is empty.

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

    def insert_at(self, index, item):
        """ Add new item to array at specific index, increase capacity if not available.

        Parameters:
            index (int): Index to to add the item at
            item (int): Item to add at the index

        Returns:
            None

        Raises:
            IndexError: If the index is out of range

        """

        if 0 > index or index > self.item_count:
            return IndexError('index out of range!')

        if self.item_count == self.array_capacity:
            self._resize(2 * self.array_capacity)

        for i in range(self.item_count, index, -1):
            self.primary_array[i] = self.primary_array[i-1]
        self.primary_array[index] = item
        self.item_count += 1

    def append(self, item):
        """ Add new item to end of array, increase capacity if not available.

        Parameters:
            item (int): Item to add to the end of the array

        Returns:
            None

        Raises:
            None

        """

        self.insert_at(self.item_count, item)

    def prepend(self, item):
        """ Add new item to beginning of array, increase capacity if not available.

        Parameters:
            item (int): Item to add to the beginning of the array

        Returns:
            None

        Raises:
            None

        """

        self.insert_at(0, item)

    def delete_at(self, index):
        """ Delete item at the given index.

        Parameters:
            index (int): Index to delete the item at

        Returns:
            None

        Raises:
            IndexError: If the index is out of range

        """

        if 0 > index or index > self.item_count - 1:
            return IndexError('index out of range!')

        while 0 <= index < self.item_count - 1:
            self.primary_array[index] = self.primary_array[index + 1]
            index += 1
        self.item_count -= 1

        if self.item_count == self.array_capacity // 4:
            self._resize(self.array_capacity // 2)

    def pop(self):
        """ Delete the item of the array and return that item.

        Parameters:
            None

        Returns:
            pop_item (int): Item that now is deleted from the array

        Raises:
            IndexError: If the array is empty

        """

        if self.is_empty():
            return IndexError('the array is empty!')

        pop_item = self.primary_array[self.item_count-1]
        self.delete_at(self.item_count-1)
        return pop_item

    def find(self, item):
        """ Delete all items that are the same as the input.

        Parameters:
            item (int): Item that that will be deleted from the array

        Returns:
            None

        Raises:
            None

        """

        index = 0
        while index < self.item_count:
            if item == self.primary_array[index]:
                return index
            index += 1
        return -1

    def remove(self, item):
        """ Delete all items that are the same as the input.

        Parameters:
            item (int): Item that that will be deleted from the array

        Returns:
            None

        Raises:
            None

        """

        find_index = self.find(item)
        while find_index >= 0:
            self.delete_at(find_index)
            find_index = self.find(item)


def main():

    print("Init and fill array.")
    x = Array()
    x.append(10)
    x.append(20)
    x.append(22)
    x.append(35)
    x.append(55)
    x.append(5)
    print(x.list())

    print("Show size and capacity.")
    print(x.size())
    print(x.capacity())

    print("Check if array is empty.")
    print(x.is_empty())

    print("Insert item at index 2.")
    x.insert_at(2, 5)
    print(x.list())

    print("Append item.")
    x.append(99)
    print(x.list())

    print("Prepend item.")
    x.prepend(2)
    print(x.list())

    print("Delete index at index 5.")
    x.delete_at(5)
    print(x.list())

    print("Pop item.")
    print(x.pop())
    print(x.list())

    print("Find the first instance of item 5.")
    print(x.find(5))

    print("Remove all instances of item 5.")
    x.remove(5)
    print(x.list())

    print("Check downsizing of array.")
    print("Array:", x.list(), ", Size:", x.size(), ", Capacity:", x.capacity())
    x.delete_at(2)
    print("Array:", x.list(), ", Size:", x.size(), ", Capacity:", x.capacity())
    x.append(444)
    print("Array:", x.list(), ", Size:", x.size(), ", Capacity:", x.capacity())
    x.append(3)
    print("Array:", x.list(), ", Size:", x.size(), ", Capacity:", x.capacity())
    x.append(40)
    print("Array:", x.list(), ", Size:", x.size(), ", Capacity:", x.capacity())
    x.append(33)
    print("Array:", x.list(), ", Size:", x.size(), ", Capacity:", x.capacity())
    x.append(94)
    print("Array:", x.list(), ", Size:", x.size(), ", Capacity:", x.capacity())


if __name__ == "__main__":
    main()
