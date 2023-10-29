import unittest
from io import StringIO
import sys
from custom_list import CustomList


def are_lists_eq(list1, list2):
    if type(list1) != type(list2):
        return False
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


class TestMySort(unittest.TestCase):
    def test_add_customlists_2_greater_1(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([3, 4, 5, 6])
        res = list1 + list2
        self.assertTrue(are_lists_eq(res, CustomList([4, 6, 8, 6])))
        self.assertTrue(are_lists_eq(list1, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list2, CustomList([3, 4, 5, 6])))

    def test_add_customlists_1_greater_2(self):
        list1 = CustomList([3, 4, 5, 6])
        list2 = CustomList([1, 2, 3])
        res = list1 + list2
        self.assertTrue(are_lists_eq(res, CustomList([4, 6, 8, 6])))
        self.assertTrue(are_lists_eq(list1, CustomList([3, 4, 5, 6])))
        self.assertTrue(are_lists_eq(list2, CustomList([1, 2, 3])))

    def test_add_customlist_with_list(self):
        list1 = CustomList([1, 2, 3])
        list2 = [3, 4, 5, 6]
        res = list1 + list2
        self.assertTrue(are_lists_eq(res, CustomList([4, 6, 8, 6])))
        self.assertTrue(are_lists_eq(list1, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list2, [3, 4, 5, 6]))

    def test_add_list_with_customlist(self):
        list1 = CustomList([1, 2, 3])
        list2 = [3, 4, 5, 6]
        res = list2 + list1
        self.assertTrue(are_lists_eq(res, CustomList([4, 6, 8, 6])))
        self.assertTrue(are_lists_eq(list1, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list2, [3, 4, 5, 6]))

    def test_add_with_empty_right(self):
        list1 = CustomList([1, 2, 3])
        list2=[]
        res = list2 + list1
        self.assertTrue(are_lists_eq(res, CustomList([1,2,3])))
        self.assertTrue(are_lists_eq(list1, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list2, []))
        list2 = CustomList([])
        res = list2 + list1
        self.assertTrue(are_lists_eq(res, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list1, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list2, CustomList([])))

    def test_add_with_empty_left(self):
        list1 = CustomList([1, 2, 3])
        list2=[]
        res = list1 + list2
        self.assertTrue(are_lists_eq(res, CustomList([1,2,3])))
        self.assertTrue(are_lists_eq(list1, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list2, []))
        list2 = CustomList([])
        res = list1 + list2
        self.assertTrue(are_lists_eq(res, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list1, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list2, CustomList([])))

    def test_add_empty(self):
        list1 = CustomList([])
        list2 = CustomList([])
        res = list1 + list2
        self.assertTrue(are_lists_eq(res, CustomList([])))
        self.assertTrue(are_lists_eq(list1, CustomList([])))
        self.assertTrue(are_lists_eq(list2, CustomList([])))

    def test_sub_customlists(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([3, 4, 5, 6])
        res = list1 - list2
        self.assertTrue(are_lists_eq(res, CustomList([-2, -2, -2, -6])))
        self.assertTrue(are_lists_eq(list1, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list2, CustomList([3, 4, 5, 6])))

    def test_sub_customlists_invert(self):
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([3, 4, 5, 6])
        res = list2 - list1
        self.assertTrue(are_lists_eq(res, CustomList([2, 2, 2, 6])))
        self.assertTrue(are_lists_eq(list1, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list2, CustomList([3, 4, 5, 6])))

    def test_sub_customlist_with_list(self):
        list1 = CustomList([1, 2, 3])
        list2 = [3, 4, 5, 6]
        res = list1 - list2
        self.assertTrue(are_lists_eq(res, CustomList([-2, -2, -2, -6])))
        self.assertTrue(are_lists_eq(list1, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list2, [3, 4, 5, 6]))

    def test_sub_list_with_customlist(self):
        list1 = CustomList([1, 2, 3])
        list2 = [3, 4, 5, 6]
        res = list2 - list1
        self.assertTrue(are_lists_eq(res, CustomList([2, 2, 2, 6])))
        self.assertTrue(are_lists_eq(list1, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list2, [3, 4, 5, 6]))

    def test_sub_with_empty_left(self):
        list1 = CustomList([1, 2, 3])
        list2 = []
        res = list2 - list1
        self.assertTrue(are_lists_eq(res, CustomList([-1,-2,-3])))
        self.assertTrue(are_lists_eq(list1, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list2, []))
        list2 = CustomList([])
        res = list2 - list1
        self.assertTrue(are_lists_eq(res, CustomList([-1, -2, -3])))
        self.assertTrue(are_lists_eq(list1, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list2, CustomList([])))

    def test_sub_with_empty_right(self):
        list1 = CustomList([1, 2, 3])
        list2 = []
        res = list1 - list2
        self.assertTrue(are_lists_eq(res, CustomList([1,2,3])))
        self.assertTrue(are_lists_eq(list1, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list2, []))
        list2 = CustomList([])
        res = list1 - list2
        self.assertTrue(are_lists_eq(res, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list1, CustomList([1, 2, 3])))
        self.assertTrue(are_lists_eq(list2, CustomList([])))

    def test_sub_empty(self):
        list1 = CustomList([])
        list2 = CustomList([])
        res = list1 - list2
        self.assertTrue(are_lists_eq(res, CustomList([])))
        self.assertTrue(are_lists_eq(list1, CustomList([])))
        self.assertTrue(are_lists_eq(list2, CustomList([])))

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
        res=-list1
        self.assertTrue(are_lists_eq(res, CustomList([-2,1,0])))
        self.assertTrue(are_lists_eq(list1, CustomList([2, -1, 0])))

    def test___str__(self):
        list1 = CustomList([2, -1, 0])
        self.assertEqual(str(list1), "List's elements: 2 -1 0 \nSum: 1")
