import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Same reasons as it is good for the queue
        # dynamic length
        self.storage = DoublyLinkedList()

    def push(self, value):
        ''' adds a value to the end of the list '''
        self.storage.add_to_tail(value)

    def pop(self):
        ''' Removes and returns the last value in the list '''
        value = self.storage.remove_from_tail()
        return value

    def len(self):
        return self.storage.length
