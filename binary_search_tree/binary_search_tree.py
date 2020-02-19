import sys
sys.path.append('../')
from queue_and_stack.dll_queue import Queue
from queue_and_stack.dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value is None:
            return

        elif self.value is None:
            self.value = value
        
        elif value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.in_order_print(node.left)

        print(node.value)

        if node.right:
            node.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        print(node.value)
        nodes = [self.left, self.right]

        while nodes:
            next_nodes = []
            for n in nodes:
                if n is None:
                    continue

                print(n.value)
                if n.left:
                    next_nodes.append(n.left)
                if n.right:
                    next_nodes.append(n.right)
            
            nodes = next_nodes
            
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        node_stack = Stack()
        def traverse_left_branch(node):
            left = node.left
            while left:
                print(left.value)

                if left.right:
                    node_stack.push(left.right)

                left = left.left

        print(node.value)
        
        if node.right:
            node_stack.push(node.right)
        
        traverse_left_branch(node)

        while len(node_stack):
            step_right = node_stack.pop()
            print(step_right.value)
            traverse_left_branch(step_right)

        # left = node.left
        # while left:
        #     print(left.value)

        #     if left.right:
        #         node_stack.push(left.right)

        #     left = left.left




    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
