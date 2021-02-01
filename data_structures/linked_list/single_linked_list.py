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
        """Init single linked list object.

        Parameters:
            None

        Returns:
            None

        Raises:
            None
        """
        self.head = None
        self.size = 0

    def __len__(self):
        """Get length of the single linked list object.

        Parameters:
            None

        Returns:
            [...] (int): Number of data nodes in the list object

        Raises:
            None
        """
        return self.size

# TODO: clear code if not needed
        #count = 0
        #current = self.head_
        # while current:
        #    count += 1
        #    current = current.get_next()
        # return count

    def __str__(self):
        """Get string representation of the single linked list object.

        Parameters:
            None

        Returns:
            output (str): String representation of the list object

        Raises:
            None
        """
        current_node = self.head
        output = ""
        while current_node:
            output += str(current_node) + " -> "
            current_node = current_node.get_next()
        return output

    def _increase_size(self):
        """Increase size attribute of single linked list object by one.

        Parameters:
            None

        Returns:
            None

        Raises:
            None
        """
        self.size += 1

    def _decrease_size(self):
        """Decrease size attribute of single linked list object by one.

        Parameters:
            None

        Returns:
            None

        Raises:
            None
        """
        if self.size > 0:
            self.size -= 1

    def get_size(self):
        """Returns number of node objects in the list.

        Parameters:
            None

        Returns:
            [...] (int): Number of items in the array

        Raises:
            None
        """
        return self.size

    def is_empty(self):
        """Returns True if the array is empty.

        Parameters:
            None

        Returns:
            [...] (bool): Indicator if array is empty

        Raises:
            None
        """
        if self.size == 0:
            return True
        else:
            return False

    def set_head(self, node):
        """Set the head attribute to a node reference.

        Parameters:
            node (Node): Reference to a node object

        Returns:
            None

        Raises:
            None
        """
        self.head = node

    # Pops an item from the front of the list

    def pop(self):
        if self.head_:
            self.head_ = self.head_.get_next()
        else:
            raise IndexError("Unable to pop from empty list")

    # Returns true if list contains the given value.
    def contains(self, value):
        found = False
        current = self.head_
        while current and not found:
            if current.get_data() == value:
                found = True
            else:
                current = current.get_next()
        return found

    # Deletes all instances of given value in list.
    def delete(self, value):
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

    # Pushes an item on the front of the list.
    def push(self, value):
        node = Node(value)
        node.set_next(self.head_)
        self.set_head(node)

    def append(self, value):
        node = Node(value)
        current = self.head_
        if not current:
            self.head_ = node
            return

        while current.get_next():
            current = current.get_next()

        current.set_next(node)


def main():
    ll = SingleLinkedList()

    print("Initial size: ", len(ll))
    ll.push(24)
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
    print("List content: ", ll)


if __name__ == "__main__":
    main()
