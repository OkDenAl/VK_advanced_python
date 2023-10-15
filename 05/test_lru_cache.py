import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_limit_greater_than_2(self):
        limit = 4
        test_cache = LRUCache(limit)
        for test_val in range(limit):
            test_cache.set(test_val, test_val)
        for test_val in range(limit):
            self.assertEqual(test_cache.get(test_val), test_val)

        self.assertEqual(test_cache.get(limit + 1), None)
        test_cache.set(limit + 1, limit + 1)
        self.assertEqual(test_cache.get(limit + 1), limit + 1)
        self.assertEqual(test_cache.get(0), None)
        self.assertEqual(test_cache.limit, limit)

    def test_limit_1(self):
        limit = 1
        test_cache = LRUCache(limit)
        for test_val in range(limit + 3):
            test_cache.set(test_val, test_val)
        for test_val in range(limit + 2):
            self.assertEqual(test_cache.get(test_val), None)

        self.assertEqual(test_cache.get(limit + 2), limit + 2)

    def test_limit_2(self):
        limit = 2
        test_cache = LRUCache(limit)
        for test_val in range(limit):
            test_cache.set(test_val, test_val)
        for test_val in range(limit):
            self.assertEqual(test_cache.get(test_val), test_val)

        self.assertEqual(test_cache.get(limit + 1), None)
        self.assertEqual(test_cache.get(0), 0)
        test_cache.set(limit + 1, limit + 1)
        self.assertEqual(test_cache.get(limit + 1), limit + 1)
        self.assertEqual(test_cache.get(0), 0)
        self.assertEqual(test_cache.get(1), None)

    def test_reassigned_value(self):
        test_cache = LRUCache(2)
        test_cache.set(2, 1)
        test_cache.set(2, 2)
        self.assertEqual(test_cache.get(2), 2)
        test_cache.set(1, 1)
        test_cache.set(4, 1)
        self.assertEqual(test_cache.get(2), None)
        self.assertEqual(test_cache.get(4), 1)
        test_cache.set(4, 2)
        self.assertEqual(test_cache.get(4), 2)
        self.assertEqual(test_cache.get(1), 1)

    def test_default_limit(self):
        test_cache = LRUCache()
        self.assertEqual(test_cache.limit, 42)

    def test_invalid_limit(self):
        test_cache = LRUCache(-1)
        self.assertEqual(test_cache.limit, 42)
