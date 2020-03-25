import sys
sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


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
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass




# test = BinarySearchTree(7)
# test.insert(3)
# test.insert(5)
# test.insert(2)
# test.insert(9)
# test.insert(10)
# test.insert(8)
# print(test.get_max())


