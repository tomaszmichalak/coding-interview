import logging
import sys

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))

class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev: ListNode = None
        self.next: ListNode = None
    

class LRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            self.capacity = 5
        else:
            self.capacity = capacity
        self.cache = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            # move the node to the end (most recent) of the list
            node = self.cache[key]
            updated = self.moveTail(key, node.val)
            self.cache[key] = updated
            return updated.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.size >= self.capacity:
            if key in self.cache:
                # remove node from list
                # add at the end (most recent) of the list
                node = self.moveTail(key, value)
                self.cache[key] = node
            else:
                # remove least node from list
                # remove from cache
                # add at the end (most recent) of the list
                # add to cache
                deleted = self.removeHead()
                del self.cache[deleted.key]
                node = self.addTail(key, value)
                self.cache[key] = node
        else:
            if key in self.cache:
                # remove node from list
                # add at the end (most recent) of the list
                node = self.moveTail(key, value)
                self.cache[key] = node
                return node.val
            else:
                # add at the end (most recent) of the list
                # add to cache
                node = self.addTail(key, value)
                self.cache[key] = node
                self.size += 1

    def addTail(self, key: int, value: int) -> ListNode:
        prev = self.tail.prev
        node = ListNode(key, value)
        node.next = self.tail
        node.prev = prev
        prev.next = node
        self.tail.prev = node
        return node
    
    def moveTail(self, key: int, value: int) -> ListNode:
        node = self.cache[key]
        next = node.next
        prev = node.prev
        next.prev = prev
        prev.next = next
        return self.addTail(key, value)
    
    def removeHead(self) -> ListNode:
        deleted = self.head.next
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return deleted

    def print_cache(self):
        node = self.head.next # skip fake head
        result = []
        while node:
            result.append((node.key, node.val))
            node = node.next
        return result[:-1] # skip fake tail

def test_cache_minimal_capacity():
    lru_cache = LRUCache(1)
    lru_cache.put(1, 1)
    assert lru_cache.get(1) == 1
    assert lru_cache.print_cache() == [(1,1)]

def test_cache_over_capacity():
    lru_cache = LRUCache(1)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    assert lru_cache.get(1) == -1
    assert lru_cache.get(2) == 2
    assert lru_cache.print_cache() == [(2,2)]

def test_cache_update_value():
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(1, 2)
    assert lru_cache.get(1) == 2
    assert lru_cache.print_cache() == [(1,2)]

def test_cache_update_value_over_capacity():
    lru_cache = LRUCache(1)
    lru_cache.put(1, 1)
    lru_cache.put(1, 2)
    assert lru_cache.get(1) == 2
    assert lru_cache.print_cache() == [(1,2)]

def test_cache_get_tail_update():
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    assert lru_cache.print_cache() == [(1,1),(2,2)]
    assert lru_cache.get(1) == 1
    assert lru_cache.print_cache() == [(2,2),(1,1)]

def test_complex_scenario():
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)               # cache is [(1,1)]
    lru_cache.put(2, 2)               # cache is [(1,1),(2,2)]
    assert lru_cache.get(1) == 1      # return 1, cache is [(2,2),(1,1)]
    lru_cache.put(3, 3)               # evicts key 2, cache is # cache is [(1,1),(2,2)]
    assert lru_cache.get(2) == -1     # returns -1 (not found)
    lru_cache.put(4, 4)               # evicts key 1, cache is {4=4, 3=3}
    assert lru_cache.get(1) == -1     # return -1 (not found)
    assert lru_cache.get(3) == 3      # return 3
    assert lru_cache.get(4) == 4      # return 4