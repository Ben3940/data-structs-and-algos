from Nodes.Node import Node


class LinkedList:

    def __init__(self, head=None):
        self.length = 1 if head else 0
        self.tail = self.head = head

    # Get element at idx
    def get(self, idx):
        # Out-of-bounds idx or there are no items in LinkedList
        if not self.head or idx < 0 or idx > self.length:
            return

        count = 0
        node = self.head

        # Walk list until idx
        while count < idx:
            node = node.get_next()
            count += 1
        return node.get_value()

    # Set element at idx
    def set(self, idx, value):
        # Out-of-bounds idx or there are no items in LinkedList
        if not self.head or idx < 0 or idx > self.length:
            return
        count = 0
        node = self.head

        # Walk list until idx
        while count < idx:
            node = node.get_next()
            count += 1
        node.set_value(value)

    # Add element to tail of LinkedList
    def push(self, value):
        self.length += 1
        node = Node(value)
        if not self.tail:
            self.head = self.tail = node
            return
        self.tail.set_next_node(node)
        self.tail = node
        return

    # Remove and return value of node at head of LinkedList
    def pop(self):
        if not self.head:
            return

        self.length -= 1
        node = self.head
        self.head = self.head.get_next()

        # List is empty and tail needs to be set to None, that way new elements are push() properly later
        # No need to set head to None, since it will be None from get_next() above when length is 0 or less
        if self.length <= 0:
            self.tail = None

        return node.get_value()

    # Return length of LinkedList
    def size(self):
        return self.length
