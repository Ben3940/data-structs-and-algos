from Node import Node


class Stack:

    def __init__(self):
        self.length = 0
        self.tail = None

    def push(self, value):
        node = Node(value)
        self.length += 1
        if not self.tail:
            self.tail = node
        else:
            node.set_next_node(self.tail)
            self.tail = node

    def pop(self):
        if not self.tail:
            return

        self.length -= 1
        value = self.tail.get_value()
        self.tail = self.tail.get_next()

        if self.length <= 0:
            self.tail = None
        return value

    def peek(self):
        if self.tail:
            return self.tail.get_value()
