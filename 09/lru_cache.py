import argparse
from logger import init, add_filter, add_stdout

log = init()


class LRUCache:
    class ListNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
            log.debug("list node successfully created with key %s, value %s", key, value)

    def __init__(self, limit=42):
        if limit <= 0:
            limit = 42
        self.__cache = {}
        self.limit = limit
        self.__head = None
        self.__tail = None
        log.debug("lru cache successfully created with capacity %d", limit)

    def get(self, key):
        if key in self.__cache:
            log.info("Get:\t key %s was found in cache", key)
            node = self.__cache[key]
            self.__delete_from_list(node)
            self.__add_to_head(node)
            return node.value
        log.warning("Get:\t key %s was not found in cache", key)
        return None

    def set(self, key, value):
        if key in self.__cache:
            log.info("Set:\t changing value for existing key %s to value %s", key, value)
            node = self.__cache[key]
            self.__delete_from_list(node)
            self.__cache[key] = self.ListNode(key, value)
            self.__add_to_head(self.__cache[key])
        else:
            log.info("Set:\t add new key %s with value %s", key, value)
            if len(self.__cache) >= self.limit:
                log.warning("Set:\t overflow, remove last element %s", self.__tail.key)
                self.__delete_from_tail()
            node = self.ListNode(key, value)
            self.__cache[key] = node
            self.__add_to_head(node)

    def __add_to_head(self, node):
        node.prev = None
        log.debug("add new node with key: %s and value: %s to head", node.key, node.value)
        if self.__head is None:
            self.__head = self.__tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def __delete_from_list(self, node):
        log.debug("delete node with key: %s and value: %s from cache", node.key, node.value)
        if self.__head == self.__tail:
            self.__head = self.__tail = None
        elif node == self.__tail:
            node.prev.next = None
            self.__tail = node.prev
        elif node == self.__head:
            node.next.prev = None
            self.__head = node.next
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def __delete_from_tail(self):
        log.debug("delete node from tail")
        if self.__head == self.__tail:
            del self.__cache[self.__tail.key]
            self.__head = self.__tail = None
        else:
            self.__tail.prev.next = None
            del self.__cache[self.__tail.key]
            self.__tail = self.__tail.prev


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", action="store_true")
    parser.add_argument("-f", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.s:
        log = add_stdout(log)
    if args.f:
        log = add_filter(log)

    cache = LRUCache(2)
    cache.set("k1", "1")
    cache.set("k2", "2")
    assert cache.get("k3") is None
    assert cache.get("k2") == "2"
    assert cache.get("k1") == "1"
    cache.set("k4", "3")
    cache.set("k4", "3")
