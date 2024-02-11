import unittest
from random import shuffle
from copy import deepcopy
from BubbleSort import bubble_sort
from BinarySearch import binary_search


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        arr1 = [x for x in range(0, 20)]
        arr2 = [x for x in range(-20, 20)]
        arr3 = list()

        arr1_true = deepcopy(arr1)
        arr2_true = deepcopy(arr2)

        shuffle(arr1)
        shuffle(arr2)
        bubble_sort(arr1)
        bubble_sort(arr2)
        bubble_sort(arr3)

        self.assertEqual(arr1, arr1_true)
        self.assertEqual(arr2, arr2_true)
        self.assertEqual(arr3, list())


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        arr1 = [x for x in range(0, 10)]
        arr2 = list()

        test1 = binary_search(arr1, 5)
        test2 = binary_search(arr1, 3)
        test3 = binary_search(arr1, 12)
        test4 = binary_search(arr2, 2)

        self.assertEqual(test1, 5)
        self.assertEqual(test2, 3)
        self.assertEqual(test3, None)
        self.assertEqual(test4, None)
