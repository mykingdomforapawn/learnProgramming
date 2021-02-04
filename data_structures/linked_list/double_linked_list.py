"""Simple implementation of double linked lists with sentinels. """


class Node:
    """Implemetation of a list node. """

    def __init__(self, data=None, next=None, prev=None):
        """Init node object.

        Parameters:
            data (...): Data that is stored in this node
            next (Node): Reference to the next node in the list
            prev (Node): Reference to the previous node in the list

        Returns:
            None

        Raises:
            None
        """
        self._data = data
        self._next = next
        self._prev = prev

    def __str__(self):
        """Get string representation of the data from a node.

        Parameters:
            None

        Returns:
            [...] (...): String representation of the data that is stored in this node object

        Raises:
            None
        """
        return str(self._data)

    def get_data(self):
        """Get data from a node object.

        Parameters:
            None

        Returns:
            [...] (...): Data that is stored in this node object

        Raises:
            None
        """
        return self._data

    def set_data(self, data):
        """Set data in a node object.

        Parameters:
            data (...): Data that will be stored in this node

        Returns:
            None

        Raises:
            None
        """
        self._data = data

    def get_next(self):
        """Get the next node object after this one.

        Parameters:
            None

        Returns:
            [...] (Node): Next node object after this one

        Raises:
            None
        """
        return self._next

    def get_prev(self):
        """Get the previous node object before this one.

        Parameters:
            None

        Returns:
            [...] (Node): Previous node object before this one

        Raises:
            None
        """
        return self._prev

    def set_next(self, next):
        """Set the reference to the next node object after this one.

        Parameters:
            next (Node): Reference to the next node in the list

        Returns:
            None

        Raises:
            None
        """
        self._next = next

    def set_prev(self, prev):
        """Set the reference to the previous node object before this one.

        Parameters:
            prev (Node): Reference to the previous node in the list

        Returns:
            None

        Raises:
            None
        """
        self._prev = prev


class SingleLinkedList(object):
    """Implemetation of a double linked list. """

    def __init__(self):
        """Init list object.

        Parameters:
            None

        Returns:
            None

        Raises:
            None
        """
        self._head = None
        self._size = 0

    def __len__(self):
        """Get length of the list object.

        Parameters:
            None

        Returns:
            [...] (int): Number of data nodes in the list object

        Raises:
            None
        """
        return self._size

    def __str__(self):
        """Get string representation of the list object.

        Parameters:
            None

        Returns:
            output (str): String representation of the list object

        Raises:
            None
        """
        current_node = self._head
        output = ""
        while current_node:
            output += str(current_node) + " -> "
            current_node = current_node.get_next()
        output += "None"
        return output

    def _increase_size(self):
        """Increase size attribute of the list object by one.

        Parameters:
            None

        Returns:
            None

        Raises:
            None
        """
        self._size += 1

    def _decrease_size(self):
        """Decrease size attribute of the list object by one.

        Parameters:
            None

        Returns:
            None

        Raises:
            None
        """
        if self._size > 0:
            self._size -= 1

    def size(self):
        """Returns number of node objects in the list.

        Parameters:
            None

        Returns:
            [...] (int): Number of items in the array

        Raises:
            None
        """
        return self._size

    def is_empty(self):
        """Returns True if the list is empty.

        Parameters:
            None

        Returns:
            [...] (bool): Indicator if array is empty

        Raises:
            None
        """
        return self._size == 0

    def set_head(self, node):
        """Set the head attribute to a node reference.

        Parameters:
            node (Node): Reference to a node object

        Returns:
            None

        Raises:
            None
        """
        self._head = node

    def insert_at(self, index, data):
        """Insert a node containing the data into the list at the index.

        Parameters:
            index (int): Index to add the node at
            data (...): Data to add to the node

        Returns:
            None

        Raises:
            IndexError: If the index is out of range
        """
        if 0 > index or index > self._size:
            return IndexError('index out of range!')

        node = Node(data)
        current_node = self._head
        current_node_idx = 0
        if current_node:
            if index == 0:
                self.set_head(node)
                node.set_next(current_node)
            else:
                while current_node_idx + 1 != index:
                    current_node = current_node.get_next()
                    current_node_idx += 1
                node.set_next(current_node.get_next())
                current_node.set_next(node)
        else:
            self.set_head(node)
        self._increase_size()

    def append(self, data):
        """Append a node containing the data at the end of the list.

        Parameters:
            data (...): Data to add to the node

        Returns:
            None

        Raises:
            None
        """
        node = Node(data)
        current_node = self._head
        if current_node:
            while current_node.get_next():
                current_node = current_node.get_next()
            current_node.set_next(node)
        else:
            self.set_head(node)
        self._increase_size()

    def prepend(self, data):
        """Prepend a node containing the data at the front of the list.

        Parameters:
            data (...): Data to add to the node

        Returns:
            None

        Raises:
            None
        """
        node = Node(data)
        node.set_next(self._head)
        self.set_head(node)
        self._increase_size()

    def delete_at(self, index):
        """Delete a node in the list at the index.

        Parameters:
            index (int): Index to add the node at

        Returns:
            None

        Raises:
            IndexError: If the index is out of range
        """
        if 0 > index or index > self._size - 1:
            return IndexError('index out of range!')

        current_node = self._head
        current_node_idx = 0
        if index == 0:
            self.set_head(current_node.get_next())
        else:
            while current_node_idx + 1 != index:
                current_node = current_node.get_next()
                current_node_idx += 1
            current_node.set_next(current_node.get_next().get_next())
        self._decrease_size()

    def pop_front(self):
        """Remove front node and return its data.

        Parameters:
            None

        Returns:
            pop_data (...): Data from the first node

        Raises:
            IndexError: If the list is empty
        """
        if self._head:
            pop_data = self._head.get_data()
            self._head = self._head.get_next()
            self._decrease_size()
            return pop_data
        else:
            return IndexError("can not pop from empty list!")

    def pop_back(self):
        """Remove last node and return its data.

        Parameters:
            None

        Returns:
            pop_data (...): Data from the last node

        Raises:
            IndexError: If the list is empty
        """
        current_node = self._head
        if not current_node:
            return IndexError("can not pop from empty list!")
        else:
            if not current_node.get_next():
                pop_data = current_node.get_data()
            else:
                while current_node.get_next().get_next():
                    current_node = current_node.get_next()
                pop_data = current_node.get_next().get_data()
                current_node.set_next(None)
            self._decrease_size()
            return pop_data

    def data_at(self, index):
        """Return data of the node at the index.

        Parameters:
            None

        Returns:
            data (...): Data from the node at the index

        Raises:
            IndexError: If the index is out of range
        """
        if 0 > index or index > self._size - 1:
            return IndexError('index out of range!')

        current_node = self._head
        current_node_idx = 0
        if current_node:
            while current_node_idx != index:
                current_node = current_node.get_next()
                current_node_idx += 1
            data = current_node.get_data()
        else:
            data = self._head
        return data

    def find(self, data):
        """Search and return the index of the next node with data equal to the input.

        Parameters:
            data (...): Data to find in the list

        Returns:
            found_node_idx (int): Index of the node that contains the same data as the input

        Raises:
            None
        """
        current_node = self._head
        current_node_idx = 0
        found_node = None
        found_node_idx = None
        while current_node and not found_node:
            if current_node.get_data() == data:
                found_node = current_node
                found_node_idx = current_node_idx
            else:
                current_node = current_node.get_next()
                current_node_idx += 1
        return found_node_idx

    def contains(self, data):
        """Returns True if the list contains the data.

        Parameters:
            data (...): Data to find in the list

        Returns:
            [...] (bool): Indicator if input data was found

        Raises:
            None
        """
        return self.find(data) != None

    def remove_first(self, data):
        """Remove the first node with data equal to the input.

        Parameters:
            data (...): Data to remove in the list

        Returns:
            None

        Raises:
            None
        """
        index = self.find(data)
        if index:
            self.delete_at(index)

    def remove_all(self, data):
        """Remove all nodes with data equal to the input.

        Parameters:
            data (...): Data to remove in the list

        Returns:
            None

        Raises:
            None
        """
        index = self.find(data)
        while index != None:
            self.delete_at(index)
            index = self.find(data)

    def reverse(self):
        """Reverse the order of nodes in the list.

        Parameters:
            None

        Returns:
            None

        Raises:
            None
        """
        previous_node = None
        current_node = self._head
        while current_node is not None:
            next_node = current_node.get_next()
            current_node.set_next(previous_node)
            previous_node = current_node
            current_node = next_node
        self._head = previous_node


def main():
    print("Init single linked list.")
    sll = SingleLinkedList()
    print("List content: ", sll)
    print("Size: ", sll.size(), "\n")

    print("Fill single linked list.")
    sll.insert_at(0, 'first_item')
    sll.insert_at(0, 'second_item')
    sll.insert_at(2, 'third_item')
    sll.append('appended_item')
    sll.append('another_appended_item')
    sll.append('another_appended_item')
    sll.prepend('prepended_item')
    sll.prepend('another_prepended_item')
    sll.prepend('another_prepended_item')
    print("List content: ", sll)
    print("Size: ", sll.size(), "\n")

    print("Show data from the list via using index.")
    print("First entry: ", sll.data_at(0))
    print("Third entry: ", sll.data_at(2))
    print("List content: ", sll)
    print("Size: ", sll.size(), "\n")

    print("Find data in the list.")
    print("Find 'prepended_item': ", sll.find('prepended_item'))
    print("Find 'prepended_item_2': ", sll.find('prepended_item_2'))
    print("Contains 'second_item': ", sll.contains('second_item'))
    print("Contains 'second_item_2': ", sll.contains('second_item_2'))
    print("List content: ", sll)
    print("Size: ", sll.size(), "\n")

    print("Remove data from the list.")
    print("Remove the first 'another_appended_item': ",
          sll.remove_first('another_appended_item'))
    print("Remove all 'another_prepended_item': ",
          sll.remove_all('another_prepended_item'))
    print("List content: ", sll)
    print("Size: ", sll.size(), "\n")

    print("Delete data from the list using the index.")
    sll.delete_at(0)
    sll.delete_at(2)
    print("List content: ", sll)
    print("Size: ", sll.size(), "\n")

    print("Pop data from the list.")
    print("Pop front: ", sll.pop_front())
    print("Pop_back: ", sll.pop_back())
    print("List content: ", sll)
    print("Size: ", sll.size(), "\n")

    print("Check 'out of range' insertion and deletion.")
    print(sll.insert_at(5, 'test'))
    print(SingleLinkedList().delete_at(0))
    print(SingleLinkedList().pop_back())
    print(SingleLinkedList().pop_front(), "\n")
    print("List content: ", sll)
    print("Size: ", sll.size(), "\n")

    print("Add a few items and reverse the list.")
    sll.append('added_back')
    sll.append('added_back_2')
    sll.prepend('added_front')
    sll.prepend('added_front_2')
    print("List content: ", sll)
    sll.reverse()
    print("List content: ", sll)
    print("Size: ", sll.size(), "\n")


if __name__ == "__main__":
    main()
