"""Simple implementation of single linked lists. """


class Node:
    """Implemetation of a list node. """

    def __init__(self, data=None, next=None):
        """Init node object.

        Parameters:
            data (...): Data that is stored in this node
            next (Node): Reference to the next node in the list

        Returns:
            None

        Raises:
            None
        """
        self.data = data
        self.next = next

    def __str__(self):
        """Get string representation of the data from a node.

        Parameters:
            None

        Returns:
            [...] (...): String representation of the data that is stored in this node object

        Raises:
            None
        """
        return str(self.data)

    def get_data(self):
        """Get data from a node object.

        Parameters:
            None

        Returns:
            [...] (...): Data that is stored in this node object

        Raises:
            None
        """
        return self.data

    def set_data(self, data):
        """Set data in a node object.

        Parameters:
            data (...): Data that will be stored in this node

        Returns:
            None

        Raises:
            None
        """
        self.data = data

    def get_next(self):
        """Get the next node object after this one.

        Parameters:
            None

        Returns:
            [...] (Node): Next node object after this one

        Raises:
            None
        """
        return self.next

    def set_next(self, next):
        """Set the reference to the next node object after this one.

        Parameters:
            next (Node): Reference to the next node in the list

        Returns:
            None

        Raises:
            None
        """
        self.next = next


class SingleLinkedList(object):
    """Implemetation of a single linked list. """

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
            None

        Raises:
            IndexError: If the list is empty
        """
        if self._head:
            pop_data = self._head.get_data()
            self._head = self._head.get_next()
            self._decrease_size()
            return pop_data
        else:
            raise IndexError("can not pop from empty list!")

    def pop_back(self):
        # removes end item and returns its value
        if self.head_:
            self.head_ = self.head_.get_next()
        else:
            raise IndexError("Unable to pop from empty list")

    def value_at(self, index):
        # returns the value of the nth item (starting at 0 for first)
        pass

    def find(self, data):
        pass

    def contains(self, value):
        # Returns true if list contains the given value.
        found = False
        current = self.head_
        while current and not found:
            if current.get_data() == value:
                found = True
            else:
                current = current.get_next()
        return found

    def remove_first(self, value):
        pass

    def remove_all(self, value):
        # Deletes all instances of given value in list.
        current = self.head_
        prev = None
        while current:
            if current.get_data() == value:
                if prev:
                    prev.set_next(current.get_next())
                else:
                    self.head_ = current.get_next()
            prev = current
            current = current.get_next()

    def reverse(self):
        pass


def main():
    print("Init single linked list.")
    sll = SingleLinkedList()
    print("List content: ", sll)
    print("Size: ", sll.size())

    print("Fill single linked list.")
    sll.insert_at(0, 'first_item')
    sll.insert_at(0, 'second_item')
    sll.insert_at(2, 'third_item')
    sll.append('appended_item')
    sll.append('another_appended_item')
    sll.prepend('prepended_item')
    sll.prepend('_another_prepended_item')
    print("List content: ", sll)
    print("Size: ", sll.size())

    print("Delete data from the list.")
    sll.delete_at(0)
    sll.delete_at(2)
    sll.delete_at(4)
    print("List content: ", sll)
    print("Size: ", sll.size())

    print("Pop data from the list.")
    print(sll.pop_front())
    # print(sll.pop_back())
    print("List content: ", sll)
    print("Size: ", sll.size())

    print("Check out of range insertion and deletion.")
    sll2 = SingleLinkedList()
    print(sll2.delete_at(0))

    # vllt zu raise IndexError umwandeln..

    #print(sll.insert_at(7, 'test'))

    """ ll.push(24)
    print("New size: ", len(ll))
    print("List content: ", ll)
    print("Pushing more")
    ll.push(6)
    ll.push(783)
    print("List content: ", ll)
    print("popping...")
    ll.pop()
    print("List content: ", ll)
    print("Does list contain 24?")
    if ll.contains(24):
        print("Yes")
    else:
        print("No")
    print("Deleting 24")
    ll.delete(24)
    print("List content: ", ll)
    print("Pushing another onto end.")
    ll.append(365)
    print("List content: ", ll) """


if __name__ == "__main__":
    main()
