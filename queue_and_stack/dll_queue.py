import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

''' 
Were going to use a dll to make the queue
This allows us to have a head and a tail
We can also create arrays of dynamic size
without using insane ammounts of memory
'''
class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # It is good for making arrays of dynamic length
        # also we already wrote the code for DLL so we
        # save a lot of time not rewriting code
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        ''' Adds a value to the end of the queue '''
        self.storage.add_to_tail(value)
        

    def dequeue(self):
        ''' Removes and returns the first value in the queue '''
        value = self.storage.remove_from_head()
        return value

    def len(self):
        ''' returns the number of values in the queue '''
        return self.storage.length
