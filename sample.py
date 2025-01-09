"""
This module implements a simple linked list and its operations.
"""

class Node:
    """
    Represents a node in a linked list.
    Stores data and a reference to the next node.
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def get_data(self):
        """Returns the data of the node."""
        return self.data

    def set_data(self, data):
        """Sets the data of the node."""
        self.data = data

    def get_next(self):
        """Returns the next node."""
        return self.next

    def set_next(self, next_node):
        """Sets the next node."""
        self.next = next_node


class LinkedList:
    """
    A simple linked list implementation with operations to
    insert at the head and print the list.
    """
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        """Insert a new node with the given data at the head of the list."""
        node = Node(data, self.head)
        self.head = node

    def print_list(self):
        """Prints the linked list elements."""
        if self.head is None:
            print("Empty linked list")
            return

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
ll1 = LinkedList()
ll1.insert_at_head(13)
ll1.insert_at_head(25)
ll1.insert_at_head(50)
ll1.insert_at_head(75)

ll1.print_list()
