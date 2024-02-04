from Node import Node


class PriorityNode(Node):

    def __init__(self, value, priority, next_node=None):
        super().__init__(value, next_node)
        self.priority = priority

    def get_priority(self):
        return self.priority

    def set_priority(self, priority):
        self.priority = priority
