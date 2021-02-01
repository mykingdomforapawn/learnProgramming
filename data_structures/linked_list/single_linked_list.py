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
        self.data_ = data
        self.next_ = next

    def __str__(self):
        """Get string representation of the data from a node.

        Parameters:
            None

        Returns:
            [...] (...): String representation of the data that is stored in this node object

        Raises:
            None
        """
        return str(self.data_)

    def get_data(self):
        """Get data from a node object.

        Parameters:
            None

        Returns:
            [...] (...): Data that is stored in this node object

        Raises:
            None
        """
        return self.data_

    def set_data(self, data):
        """Set data in a node object.

        Parameters:
            data (...): Data that will be stored in this node

        Returns:
            None

        Raises:
            None
        """
        self.data_ = data

    def get_next(self):
        """Get the next node object after this one.

        Parameters:
            None

        Returns:
            [...] (Node): Next node object after this one

        Raises:
            None
        """
        return self.next_

    def set_next(self, next):
        """Set the reference to the next node object after this one.

        Parameters:
            next (Node): Reference to the next node in the list

        Returns:
            None

        Raises:
            None
        """
        self.next_ = next
