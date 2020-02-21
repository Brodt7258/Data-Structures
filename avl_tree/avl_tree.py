"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        if self.node is None:
            self.height = -1
            return self.height
        
        if self.node.left is None and self.node.right is None:
            self.height = 0
            return self.height

        l_height, r_height = 0, 0

        if self.node.left:
            l_height = 1 + self.node.left.update_height()

        if self.node.right:
            r_height = 1 + self.node.right.update_height()

        self.height = l_height if l_height > r_height else r_height
        return self.height

        

        # height = 0

        # nodes = []
        # if self.node.left:
        #     nodes.append(self.node.left)
        # if self.node.right:
        #     nodes.append(self.node.right)

        # while nodes:
        #     height += 1
        #     next_nodes = []
        #     for n in nodes:

        #         if n.node.left:
        #             next_nodes.append(n.left.node)
        #         if n.node.right:
        #             next_nodes.append(n.right.node)

        #     nodes = next_nodes
        
        # self.height = height


    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        pass

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        pass

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        pass

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        pass
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        if key is None:
            return

        elif self.node.key is None:
            self.node.key = key
        
        elif key >= self.node.key:
            if self.node.right is None:
                self.node.right = AVLTree(key)
            else:
                self.node.right.insert(key)
        else:
            if self.node.left is None:
                self.node.left = AVLTree(key)
            else:
                self.node.left.insert(key)
