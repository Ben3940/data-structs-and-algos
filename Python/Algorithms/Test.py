import unittest
from random import shuffle
from copy import deepcopy
from BubbleSort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_sort(self):
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
