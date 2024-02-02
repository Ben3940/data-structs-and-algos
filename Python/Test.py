import unittest
from Node import Node
from Stack import Stack


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


if __name__ == "__main__":
    unittest.main()
