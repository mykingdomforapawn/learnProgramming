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


def main():

    print("Init and push items to stack.")
    x = LinkedListStack()
    x.push(10)
    x.push(20)
    print("Stack:", x.list(), ", Size:", x.size())

    print("Check if array is empty.")
    print(x.is_empty())
    print("Stack:", x.list(), ", Size:", x.size())

    print("Show the top item in the stack.")
    print(x.top())
    print("Stack:", x.list(), ", Size:", x.size())

    print("Pop items from stack.")
    print(x.pop())
    print(x.pop())
    print(x.pop())
    print("Stack:", x.list(), ", Size:", x.size())

    print("Show the top item in the stack.")
    print(x.top())
    print("Stack:", x.list(), ", Size:", x.size())


if __name__ == "__main__":
    main()
