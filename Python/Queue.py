from Node import Node


class Queue:

    def __init__(self):
        self.length = 0
        self.head = self.tail = None

    def enqueue(self, value):
        self.length += 1
        node = Node(value)

        if not self.tail:
            self.head = self.tail = node

        else:
            self.tail.set_next_node(node)
            self.tail = node

    def deque(self):
        if not self.head:
            return None

        self.length -= 1
        val = self.head.get_value()
        self.head = self.head.get_next()

        if self.length == 0:
            self.tail = None

        return val

    def peek(self):
        if self.head:
            return self.head.get_value()
