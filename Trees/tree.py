class Tree:
    
    def root(self):
        # returns the root of the tree
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, node):
        # returns the parent of the node
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, node):
        # returns the number of children that node has
        raise NotImplementedError('must be implemented by subclass')

    def children(self, node):
        # returns the nodes children
        raise NotImplementedError('must be implemented by subclass')

    def num_nodes(self):
        # retrurns the number of nodes in a tree
        raise NotImplementedError('must be implemented by subclass')

    def height(self):
        # method returns the height from the root to the deepest node
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, node):
        # returns whether the node is the root node
        return node == self.root

    def is_leaf(self, node):
        # returns whether the node is a leaf node
        return node.children == None

    def is_empty(self):
        # returns true if the tree is empty
        return self.root is not None

    def depth(self, node):
        # returns the depth of the tree from node to root
        if is_root(node):
            return 0
        else:
            return 1 + depth(node.parent)