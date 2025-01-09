class Node:
    """Represents a node in a linked list."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    """A simple linked list implementation."""
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
