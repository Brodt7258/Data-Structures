import sys
sys.path.append('../')
from doubly_linked_list.doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.storage = {}
        self.lru = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # key not found, return None
        if key not in self.storage:
            return None

        # key found, return value and update lru
        else:
            self.lru.move_to_front(self.storage[key])
            return self.storage[key].value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # key already in dict, update value and lru
        if key in self.storage:
            self.storage[key].value[1] = value
            self.lru.move_to_front(self.storage[key])
            return

        # key not in dict. add to dict, store key and val in lru
        else:
            node = self.lru.add_to_head([key, value])
            self.storage[key] = node

        # exceeded size limit, get last item in lru, and remove it from lru and dict
        if len(self.lru) > self.limit:
            removed = self.lru.remove_from_tail()
            self.storage.pop(removed[0])
