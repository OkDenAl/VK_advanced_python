class LRUCache:
    class ListNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, limit=42):
        if limit <= 0:
            limit = 42
        self.__cache = {}
        self.limit = limit
        self.__head = None
        self.__tail = None

    def get(self, key):
        if key in self.__cache:
            node = self.__cache[key]
            self.__delete_from_list(node)
            self.__add_to_head(node)
            return node.value
        return None

    def set(self, key, value):
        if key in self.__cache:
            node = self.__cache[key]
            self.__delete_from_list(node)
            self.__cache[key] = self.ListNode(key, value)
            self.__add_to_head(self.__cache[key])
        else:
            if len(self.__cache) >= self.limit:
                self.__delete_from_tail()
            node = self.ListNode(key, value)
            self.__cache[key] = node
            self.__add_to_head(node)

    def __add_to_head(self, node):
        node.prev = None
        if self.__head is None:
            self.__head = self.__tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def __delete_from_list(self, node):
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
        if self.__head == self.__tail:
            del self.__cache[self.__tail.key]
            self.__head = self.__tail = None
        else:
            self.__tail.prev.next = None
            del self.__cache[self.__tail.key]
            self.__tail = self.__tail.prev
