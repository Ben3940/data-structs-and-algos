import unittest
from Node import Node


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


if __name__ == "__main__":
    unittest.main()
