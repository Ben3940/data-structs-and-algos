import unittest
from Nodes.Node import Node
from Nodes.PriorityNode import PriorityNode
from Stack import Stack
from Queue import Queue
from PriorityQueue import PriorityQueue
from LinkedList import LinkedList


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
        self.LL = LinkedList()

    def test_get(self):
        self.assertEqual(self.LL.get(1), None)
        self.assertEqual(self.LL.get(-2), None)
        self.LL.push(4)
        self.LL.push(10)
        self.assertEqual(self.LL.get(0), 4)
        self.assertEqual(self.LL.get(1), 10)

    def test_set(self):
        self.LL.set(2, 23)
        self.assertEqual(self.LL.get(2), None)
        self.LL.push(22)
        self.LL.push(10)
        self.LL.set(0, 14)
        self.LL.set(1, 20)
        self.assertEqual(self.LL.get(0), 14)
        self.assertEqual(self.LL.get(1), 20)

    def test_push_pop(self):
        self.LL.push(0)
        self.LL.push(1)
        self.LL.push(2)
        self.assertEqual(self.LL.pop(), 0)
        self.assertEqual(self.LL.pop(), 1)
        self.assertEqual(self.LL.pop(), 2)

    def test_size(self):
        self.assertEqual(self.LL.size(), 0)
        self.LL.push(0)
        self.LL.push(1)
        self.assertEqual(self.LL.size(), 2)


if __name__ == "__main__":
    unittest.main()
