from Node import Node


class Queue:

    def __init__(self):
        self.length = 0
        self.head = self.tail = None

    def enqueue(self, value):
        # Increment Queue length for new node
        self.length += 1
        node = Node(value)

        # If no tail, make head and tail point to new node
        if not self.tail:
            self.head = self.tail = node

        else:
            # Update next node to new node before setting the new node as tail
            self.tail.set_next_node(node)
            self.tail = node

    def deque(self):
        # If no head then nothing is in Queue
        if not self.head:
            return None

        # Decrement Queue length and get current head node's value
        self.length -= 1
        val = self.head.get_value()

        # Update head to point to next node in Queue
        self.head = self.head.get_next()

        # Need to set tail to None so that in enqueue() head and tail will be set again
        if self.length == 0:
            self.tail = None

        return val

    def peek(self):
        if self.head:
            return self.head.get_value()
