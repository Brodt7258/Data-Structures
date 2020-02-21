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

        if self.node.left: l_height = self.node.left.update_height()
        if self.node.right: r_height = self.node.right.update_height()

        self.height = 1 + max(l_height, r_height)
        self.update_balance()

        return self.height

    # really shouldn't have to search down every single sub branch just to update the height
    # changes should happen downstream, upon insertion or rotation, and propagate up.
    def update_height_local(self):
        if self.node is None:
            self.height = -1
            return self.height
        
        if self.node.left is None and self.node.right is None:
            self.height = 0
            return self.height
        
        l_height, r_height = 0, 0

        if self.node.left: l_height = self.node.left.height
        if self.node.right: r_height = self.node.right.height
        
        self.height = 1 + max(l_height, r_height)
        return self.height

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        l_height, r_height = 0, 0

        if self.node.left: l_height = self.node.left.height
        if self.node.right: r_height = self.node.right.height

        self.balance = l_height - r_height

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        y, x = self.node, self.node.right.node
        T1, T2, T3 = y.left, x.left, x.right

        y.left, y.key = AVLTree(Node(y.key)), x.key
        y.left.node.left, y.left.node.right, y.right = T1, T2, T3

        y.left.update_height_local()
        y.left.update_balance()

        self.update_height_local()
        self.update_balance()


    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        y, x = self.node, self.node.left.node
        T1, T2, T3, = x.left, x.right, y.right

        y.right, y.key = AVLTree(Node(y.key)), x.key
        y.left, y.right.node.left, y.right.node.right = T1, T2, T3

        y.right.update_height_local()
        y.right.update_balance()

        self.update_height_local()
        self.update_balance()

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
