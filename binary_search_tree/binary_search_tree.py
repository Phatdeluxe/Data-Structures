import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare
        # if new < node
        if value < self.value:
            # check if empty
            if self.left == None:
                # put node in
                self.left = BinarySearchTree(value)
            # else
            else:
                # go left
                self.left.insert(value)
        # if new >= node
        else:
            # check if empty
            if self.right == None:
                # put node in
                self.right = BinarySearchTree(value)
            # else
            else:
                # go right
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if node is none
            # return False
        # if node.value == findvalue
        if self.value == target:
            # return True
            return True
        # else
        else:
            # if find < node.value
            if target < self.value:
                # if left exists
                if self.left:
                    # find(node.left)
                    return self.left.contains(target)
                # else
                else:
                    # return false
                    return False
            # else
            else:
                # if right exists
                if self.right:
                    # find(node.right)
                    return self.right.contains(target)
                else:
                    return False

    # Return the maximum value found in the tree
    def get_max(self):
        # if node to right
        if self.right:
            # get_max on right
            return self.right.get_max()
        # else
        else:
            # return node.value
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # run on self
        cb(self.value)
        # if left exists
        if self.left:
            # for_each(left)
            self.left.for_each(cb)
        # if right exists
        if self.right:
            # for_each(right)
            self.right.for_each(cb)
        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        
        print(self.value)

        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node=None):
        # create a queue
        queue = Queue()
        # add root to queue
        queue.enqueue(self)
        # while queue is not empty
        while queue.len() > 0:
        # save head in local
            node = queue.storage.head
        # remove head from queue
            queue.dequeue()
        # print saved node's value
            print(node.value.value)
        # add node's children to queue
            if node.value.left:
                queue.enqueue(node.value.left)
            if node.value.right:
                queue.enqueue(node.value.right)
        # repeat
        return


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node=None):
        # create a stack
        stack = Stack()
        # add root to stack
        stack.push(self)
        # while stack is not empty
        while stack.len() > 0:
        # save tail in local
            node_hold = stack.storage.tail
        # remove tail from stack
            stack.pop()
        # print saved node's value
            print(node_hold.value.value)
        # add node's children to stack
            if node_hold.value.left:
                stack.push(node_hold.value.left)
            if node_hold.value.right:
                stack.push(node_hold.value.right)
        # repeat

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass




test = BinarySearchTree(1)
test.insert(8)
test.insert(5)
test.insert(7)
test.insert(6)
test.insert(3)
test.insert(4)
test.insert(2)
test.bft_print()
print('###########')
test.dft_print()