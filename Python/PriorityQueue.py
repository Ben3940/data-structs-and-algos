from Queue import Queue
from Nodes.PriorityNode import PriorityNode


class PriorityQueue(Queue):

    # Priority can be ordered in either 'ascending' or 'descending' order (default: ascending order)
    def __init__(self, ASCD=True):
        super().__init__()
        self.ASCD = ASCD

    # Enqueues values in ascending order
    def enqueue_ascending(self, p_node):
        curr_node = prev_node = self.head
        while curr_node:
            if p_node.get_priority() < curr_node.get_priority():
                break
            prev_node = curr_node
            curr_node = curr_node.get_next()
        # Insert p_node between prev_node and curr_node
        p_node.set_next_node(curr_node)
        prev_node.set_next_node(p_node)

    # Enqueues values in descending order
    def enqueue_descending(self, p_node):
        prev_node = None
        curr_node = self.head

        while curr_node:
            if p_node.get_priority() >= curr_node.get_priority():
                break
            prev_node = curr_node
            curr_node = curr_node.get_next()

        p_node.set_next_node(curr_node)
        # If prev_node, then update it to point to newly created p_node
        if prev_node:
            prev_node.set_next_node(p_node)

        # Update head pointer to newly created _p_node
        else:
            self.head = p_node

    # Abstracts enqueuing ordering to provide "generic" enqueue method
    def enqueue(self, value, priority):
        self.length += 1
        p_node = PriorityNode(value, priority)

        # If no head then set p_node as head, regardless of ordering
        if not self.head:
            self.head = self.tail = p_node
            return

        if self.ASCD:
            self.enqueue_ascending(p_node)
        else:
            self.enqueue_descending(p_node)

    # Display value and priority of each node in PriorityQueue
    def display(self):
        if not self.head:
            return
        curr_node = self.head
        while curr_node:
            print(f"Val: {curr_node.get_value()} Pri: {curr_node.get_priority()}")
            curr_node = curr_node.get_next()
