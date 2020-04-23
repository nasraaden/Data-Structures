from doubly_linked_list import DoublyLinkedList


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
        self.amount = 0
        self.list = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # if key is not in the storage of the list
        if key not in self.storage:
            return None
        # if key does exist, make it the new tail and return value
        else:
            node = self.storage[key]
            self.list.move_to_end(node)
            return node.value[1]

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
        # if key already exists
        if key in self.storage:
            # override the key,add the value
            node = self.storage[key]
            node.value = (key, value)
            # move to the tail which is the most recent
            self.list.move_to_end(node)
            return
        # we need to check to see if capacity has been reached
        if len(self.list) == self.limit:
            # if we reached capacity, we need to delete the current head
            current_head = self.list.head.value[0]
            del self.storage[current_head]
            self.list.remove_from_head()
        # if capacity hasn't been reached we need to add to tail
        self.list.add_to_tail((key, value))
        # update the storage
        self.storage[key] = self.list.tail
