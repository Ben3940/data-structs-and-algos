from Node import Node


class Stack:
    def __init__(self):
        self.length = 0
        self.tail = None

    def push(self, value):
        # Create node to push to Stack, increment Stack length
        node = Node(value)
        self.length += 1

        # If no tail, node is only item in Stack
        if not self.tail:
            self.tail = node
        else:
            # node's next needs to point to tail before updating tail pointer
            node.set_next_node(self.tail)
            self.tail = node

    def pop(self):
        # Stack is empty
        if not self.tail:
            return

        # Decrement Stack length and get value of node being poped off
        self.length -= 1
        value = self.tail.get_value()

        # Move tail pointer to next item in Stack
        self.tail = self.tail.get_next()

        if self.length <= 0:
            self.tail = None
        return value

    def peek(self):
        # If tail exist, we can peek
        if self.tail:
            return self.tail.get_value()
