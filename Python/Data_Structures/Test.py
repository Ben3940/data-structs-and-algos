import unittest
from Nodes.Node import Node
from Nodes.PriorityNode import PriorityNode
from Stack import Stack
from Queue import Queue
from PriorityQueue import PriorityQueue
from LinkedList import LinkedList
from Nodes.BinaryTreeNode import BinaryTreeNode


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

    def test_push_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_peek(self):
        self.assertEqual(self.stack.peek(), None)
        self.stack.push(6)
        self.assertEqual(self.stack.peek(), 6)


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue_deque(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.deque(), 1)
        self.assertEqual(self.queue.deque(), 2)

    def test_peek(self):
        self.assertEqual(self.queue.peek(), None)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(), 1)


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.ARR = [
            {"value": "A", "priority": 1},
            {"value": "G", "priority": 7},
            {"value": "C", "priority": 3},
            {"value": "A", "priority": 1},
            {"value": "E", "priority": 5},
        ]
        self.ASCD_answers = ["A", "A", "C", "E", "G"]
        self.DESC_answers = ["G", "E", "C", "A", "A"]

    def test_enqueue_ASCD(self):
        p_queue = PriorityQueue(ASCD=True)
        for pair in self.ARR:
            p_queue.enqueue(pair["value"], pair["priority"])

        for answer in self.ASCD_answers:
            self.assertEqual(p_queue.deque(), answer)

    def test_enqueue_DESC(self):
        p_queue = PriorityQueue(ASCD=False)
        for pair in self.ARR:
            p_queue.enqueue(pair["value"], pair["priority"])

        for answer in self.DESC_answers:
            self.assertEqual(p_queue.deque(), answer)


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_get(self):
        self.assertEqual(self.linked_list.get(1), None)
        self.assertEqual(self.linked_list.get(-2), None)
        self.linked_list.push(4)
        self.linked_list.push(10)
        self.assertEqual(self.linked_list.get(0), 4)
        self.assertEqual(self.linked_list.get(1), 10)

    def test_set(self):
        self.linked_list.set(2, 23)
        self.assertEqual(self.linked_list.get(2), None)
        self.linked_list.push(22)
        self.linked_list.push(10)
        self.linked_list.set(0, 14)
        self.linked_list.set(1, 20)
        self.assertEqual(self.linked_list.get(0), 14)
        self.assertEqual(self.linked_list.get(1), 20)

    def test_push_pop(self):
        self.linked_list.push(0)
        self.linked_list.push(1)
        self.linked_list.push(2)
        self.assertEqual(self.linked_list.pop(), 0)
        self.assertEqual(self.linked_list.pop(), 1)
        self.assertEqual(self.linked_list.pop(), 2)

    def test_size(self):
        self.assertEqual(self.linked_list.size(), 0)
        self.linked_list.push(0)
        self.linked_list.push(1)
        self.assertEqual(self.linked_list.size(), 2)


class TestBinaryTreeNode(unittest.TestCase):
    def setUp(self):
        self.tree_node = BinaryTreeNode(1, "A")

    def test_get_set_value(self):
        self.assertEqual(self.tree_node.get_value(), 1)
        self.tree_node.set_value(2)
        self.assertEqual(self.tree_node.get_value(), 2)

    def test_get_set_key(self):
        self.assertEqual(self.tree_node.get_key(), "A")
        self.tree_node.set_key("C")
        self.assertEqual(self.tree_node.get_key(), "C")

    def test_get_set_left(self):
        self.assertEqual(self.tree_node.get_left(), None)
        tree_node_2 = BinaryTreeNode(3, "G")
        self.tree_node.set_left(tree_node_2)
        self.assertEqual(self.tree_node.get_left().get_value(), 3)

    def test_get_set_right(self):
        self.assertEqual(self.tree_node.get_right(), None)
        tree_node_2 = BinaryTreeNode(5, "I")
        self.tree_node.set_right(tree_node_2)
        self.assertEqual(self.tree_node.get_right().get_value(), 5)


if __name__ == "__main__":
    unittest.main()
