"""Implementation of a stack based on an a single linked list. """


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


class LinkedListStack:
    """Stack implemetation class. """

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

    def push(self, data):
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

    def top(self):
        """Return data of the front node.

        Parameters:
            None

        Returns:
            top_data (...): Data from the first node

        Raises:
            IndexError: If stack is empty
        """

        if self.is_empty():
            return IndexError('the stack is empty!')

        top_data = self._head.get_data()
        return top_data

    def pop(self):
        """Remove front node and return its data.

        Parameters:
            None

        Returns:
            pop_data (...): Data from the first node

        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            return IndexError('the stack is empty!')

        pop_data = self._head.get_data()
        self._head = self._head.get_next()
        self._decrease_size()
        return pop_data


def main():

    print("Init and push items to stack.")
    x = LinkedListStack()
    x.push(10)
    x.push(20)
    print("Stack:", x, ", Size:", x.size())

    print("Check if array is empty.")
    print(x.is_empty())
    print("Stack:", x, ", Size:", x.size())

    print("Show the top item in the stack.")
    print(x.top())
    print("Stack:", x, ", Size:", x.size())

    print("Pop items from stack.")
    print(x.pop())
    print(x.pop())
    print(x.pop())
    print("Stack:", x, ", Size:", x.size())

    print("Show the top item in the stack.")
    print(x.top())
    print("Stack:", x, ", Size:", x.size())


if __name__ == "__main__":
    main()
