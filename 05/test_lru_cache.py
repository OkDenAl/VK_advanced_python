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

        self.assertEqual(test_cache.get(5), None)
        test_cache.set(5, 5)
        self.assertEqual(test_cache.get(5), 5)
        self.assertEqual(test_cache.get(0), None)
        self.assertEqual(test_cache.limit, limit)

    def test_limit_1(self):
        limit = 1
        test_cache = LRUCache(limit)
        for test_val in range(4):
            test_cache.set(test_val, test_val)
        for test_val in range(3):
            self.assertEqual(test_cache.get(test_val), None)

        self.assertEqual(test_cache.get(3), 3)

    def test_limit_2(self):
        limit = 2
        test_cache = LRUCache(limit)
        for test_val in range(limit):
            test_cache.set(test_val, test_val)
        for test_val in range(limit):
            self.assertEqual(test_cache.get(test_val), test_val)

        self.assertEqual(test_cache.get(3), None)
        self.assertEqual(test_cache.get(0), 0)
        test_cache.set(3, 3)
        self.assertEqual(test_cache.get(3), 3)
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

    def test_like_in_task(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k3"),None)
        self.assertEqual(cache.get("k2"),"val2")
        self.assertEqual(cache.get("k1"),"val1")

        cache.set("k3", "val3")

        self.assertEqual(cache.get("k3"),"val3")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual (cache.get("k1") ,"val1")

    def test_update_existing_key(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k1","val3")
        cache.set("k3","val")

        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k3"),"val")
        self.assertEqual (cache.get("k1") ,"val3")


