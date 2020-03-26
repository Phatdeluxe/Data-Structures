import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

'''
My implementation O(n)
'''

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
        self.storage = DoublyLinkedList()
        self.keys = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if the key exists
        if key in self.keys:
            # using an iterator to move through our list
            node = self.storage.head
            # Used to iterate through the linked-list
            while True:
                if node.value[0] == key:
                    self.storage.add_to_tail((key, node.value))
                    self.storage.delete(node)
                    break
                else:
                    node = node.next
            # return value
            return self.keys[key]
        # else
        else:
            return None


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
        # if key exists replace
        if key in self.keys:
        # delete old node
            node = self.storage.head
            while True:
                if node.value[0] == key:
                    self.storage.delete(node)
                    break
                else:
                    node = node.next
        # add new value and node
            self.storage.add_to_tail((key, value))
            self.keys[key] = value
        # elif cache full
        elif self.limit == len(self.storage):
            # remove key from keys
            self.keys.pop(self.storage.head.value[0])
            # remove head
            self.storage.remove_from_head()
            # add to tail
            self.storage.add_to_tail((key, value))
            # add to keys
            self.keys[key] = value
        # else add to tail
        else:
            # add to tail
            self.storage.add_to_tail((key, value))
            # add to dict
            self.keys[key] = value



# test = LRUCache(limit=3)

# test.set(1, 2)
# print(test.keys)
# print(len(test.storage))
# test.set(3, 4)
# print(test.keys)
# print(len(test.storage))
# test.set(5, 6)
# print(test.keys)
# print(len(test.storage))
# test.set(7, 8)
# print(test.keys)
# print(len(test.storage))
# test.set(5, 9)
# print(test.keys)
# print(len(test.storage))

# print(test.get(7))



'''
Brian's Implemetation O(1)
'''

class LRUCache1:

    def __init__(self, limit=10):
        self.limit = limit
        # self.size = 0
        self.order = DoublyLinkedList()
        self.storage = {}

    def get(self, key):
        # Key is not in cache -- return cache
        if key not in self.storage:
            return None

        # key in cache
        else:
            # move it to tail
            node = self.storage[key]
            self.order.move_to_end(node)
            # return value
            return node.value[1]


    def set(self, key, value):
        # Different scenarios

        # item/key already exist
        if key in self.storage:
            # overwrite value
            # wher is the value stored?
            node = self.storage[key]
            node.value = (key, value)
            # move to tail (most recently used)
            self.order.move_to_end(node)
            return

        # size at limit
        if len(self.order) == self.limit:
            # remove oldest entry
            index_of_oldest = self.order.head.value[0]
            del self.storage[index_of_oldest]
            self.order.remove_from_head()

        # add to order
        self.order.add_to_tail((key, value))
        # add to storage
        self.storage[key] = self.order.tail
