import unittest
from Nodes.Node import Node
from Nodes.PriorityNode import PriorityNode
from Stack import Stack
from Queue import Queue


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Node(0)

    def test_get_value(self):
        self.assertEqual(self.node.get_value(), 0)

    def test_set_value(self):
        self.node.set_value(1)
        self.assertEqual(self.node.get_value(), 1)

    def test_set_next_node(self):
        node = Node(0)
        self.node.set_next_node(node)
        self.assertEqual(self.node.get_next(), node)


class TestPriorityNode(unittest.TestCase):
    def setUp(self):
        self.p_node = PriorityNode(value=2, priority=4)

    def test_get_priority(self):
        self.assertEqual(self.p_node.get_priority(), 4)

    def test_set_priority(self):
        self.p_node.set_priority(1)
        self.assertEqual(self.p_node.get_priority(), 1)


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), None)

        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)
        self.assertEqual(self.stack.pop(), 5)
        self.stack.pop()
        self.assertEqual(self.stack.pop(), 3)

    def test_peek(self):
        self.assertEqual(self.stack.peek(), None)
        self.stack.push(6)
        self.assertEqual(self.stack.peek(), 6)


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.deque(), 1)
        self.assertEqual(self.queue.deque(), 2)

    def test_deque(self):
        self.assertEqual(self.queue.deque(), None)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.assertEqual(self.queue.deque(), 3)
        self.assertEqual(self.queue.deque(), 4)

    def test_peek(self):
        self.assertEqual(self.queue.peek(), None)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(), 1)


if __name__ == "__main__":
    unittest.main()
