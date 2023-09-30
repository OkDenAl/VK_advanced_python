import unittest
from io import StringIO
import sys
from custom_list import CustomList


class TestMySort(unittest.TestCase):
    def test_add_customlists(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([3, 4, 5, 6])
        self.assertListEqual(list1 + list2, CustomList([4, 6, 8, 6]))

    def test_add_customlist_with_list(self):
        list1 = CustomList([1, 2, 3])
        self.assertListEqual(list1 + [3, 4, 5, 6], CustomList([4, 6, 8, 6]))

    def test_add_list_with_customlist(self):
        list1 = CustomList([1, 2, 3])
        self.assertListEqual([3, 4, 5, 6] + list1, CustomList([4, 6, 8, 6]))

    def test_add_with_empty(self):
        list1 = CustomList([1, 2, 3])
        self.assertListEqual([] + list1, CustomList([1, 2, 3]))

    def test_add_empty(self):
        self.assertListEqual(CustomList([]) + CustomList([]), CustomList([]))

    def test_sub_customlists(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([3, 4, 5, 6])
        self.assertListEqual(list1 - list2, CustomList([-2, -2, -2, -6]))

    def test_sub_customlists_invert(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([3, 4, 5, 6])
        self.assertListEqual(list2 - list1, CustomList([2, 2, 2, 6]))

    def test_sub_customlist_with_list(self):
        list1 = CustomList([1, 2, 3])
        self.assertListEqual(list1 - [3, 4, 5, 6], CustomList([-2, -2, -2, -6]))

    def test_sub_list_with_customlist(self):
        list1 = CustomList([1, 2, 3])
        self.assertListEqual([3, 4, 5, 6] - list1, CustomList([2, 2, 2, 6]))

    def test_sub_with_empty(self):
        list1 = CustomList([1, 2, 3])
        self.assertListEqual([] - list1, CustomList([-1, -2, -3]))

    def test_sub_empty(self):
        self.assertListEqual(CustomList([]) - CustomList([]), CustomList([]))

    def test_equal_true(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([6])
        self.assertEqual(list1 == list2, True)

    def test_equal_false(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([1, 2, 4])
        self.assertEqual(list1 == list2, False)

    def test_not_equal_false(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([6])
        self.assertEqual(list1 != list2, False)

    def test_not_equal_true(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([1, 2, 4])
        self.assertEqual(list1 != list2, True)

    def test_greater_than_true(self):
        list1 = CustomList([10])
        list2 = CustomList([1, 2, 4])
        self.assertEqual(list1 > list2, True)

    def test_greater_than_false(self):
        list1 = CustomList([1, 1, 1, 1])
        list2 = CustomList([1, 2, 4])
        self.assertEqual(list1 > list2, False)

    def test_less_than_true(self):
        list1 = CustomList([0, 0, 0, 0, 0])
        list2 = CustomList([1, 2, 4])
        self.assertEqual(list1 < list2, True)

    def test_less_than_false(self):
        list1 = CustomList([1, 1, 1, 10])
        list2 = CustomList([1, 2, 4])
        self.assertEqual(list1 < list2, False)

    def test_less_equal_true(self):
        list1 = CustomList([7])
        list2 = CustomList([1, 2, 4])
        self.assertEqual(list1 <= list2, True)

    def test_less_equal_false(self):
        list1 = CustomList([1, 1, 1, 10])
        list2 = CustomList([1, 2, 4])
        self.assertEqual(list1 <= list2, False)

    def test_greater_equal_true(self):
        list1 = CustomList([7])
        list2 = CustomList([1, 2, 4])
        self.assertEqual(list1 >= list2, True)

    def test_greater_equal_false(self):
        list1 = CustomList([1, 1, 1, 1])
        list2 = CustomList([1, 2, 4])
        self.assertEqual(list1 >= list2, False)

    def test_neg(self):
        list1 = CustomList([2, -1, 0])
        self.assertListEqual(-list1, CustomList([-2, 1, 0]))

    def test___str__(self):
        list1 = CustomList([2, -1, 0])
        captured_output = StringIO()
        sys.stdout = captured_output
        print(list1)
        self.assertEqual(captured_output.getvalue(),
                         "List's elements: 2 -1 0 \nSum: 1\n")
