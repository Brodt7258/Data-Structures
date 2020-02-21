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
        l_height, r_height = -1, -1

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
    # kind of just hate the premise of this. It makes no sense to assemble the entire tree, and only THEN try to rebalance everything at once
    # that's the sort of thing that should be handled in small steps on subtrees as values are inserted.
    def rebalance(self):
        self.update_height()

        # a tree cannot be unbalanced without a height of at least 2
        if self.height < 2:
            return

        # look down the branches, and handle any imbalances lower on the tree
        # before trying to fix it at this level
        if self.node.left:
            self.node.left.rebalance()
        
        if self.node.right:
            self.node.right.rebalance()

        # note any changes that occured on the downstream rebalance
        self.update_height_local()
        self.update_balance()

        # Left hand imbalances
        if self.balance > 1:
            ll_sub_height = self.node.left.node.left.height if self.node.left.node.left else -1
            lr_sub_height = self.node.left.node.right.height if self.node.left.node.right else -1

            # 'Left Left' case
            if ll_sub_height > lr_sub_height:
                self.right_rotate()
            # 'Left Right' case
            else:
                self.node.left.left_rotate()
                self.right_rotate()

        # Right hand imbalances
        elif self.balance < -1:
            rl_sub_height = self.node.right.node.left.height if self.node.right.node.left else -1
            rr_sub_height = self.node.right.node.right.height if self.node.right.node.right else -1
            # 'Right Right' case
            if rl_sub_height < rr_sub_height:
                self.left_rotate()
            # 'Right Left' case
            else:
                self.node.right.right_rotate()
                self.left_rotate()
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    # should probably rewrite this to use a stack, and a new rebalancing method that doesn't make uncessary recursive calls down the tree
    def insert(self, key):
        if key is None:
            return

        elif self.node is None:
            self.node = Node(key)
        
        elif key >= self.node.key:
            if self.node.right is None:
                self.node.right = AVLTree(Node(key))
            else:
                self.node.right.insert(key)
        else:
            if self.node.left is None:
                self.node.left = AVLTree(Node(key))
            else:
                self.node.left.insert(key)
        

        self.update_height_local()
        self.update_balance()

        if self.balance > 1 or self.balance < -1:
            self.rebalance()
