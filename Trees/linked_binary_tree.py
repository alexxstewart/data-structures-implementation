import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import Tree

class LinkedBinaryTree(Tree):

    class _Node:
        def __init__(self, parent=None):
            self._parent = parent

    def __init__(self):
        pass

    def parent(self):
        pass

    def right(self):
        pass

    def left(self):
        pass

    def length(self):
        pass

    def num_children(self):
        pass

    def add_root(self):
        pass

    def add_left(self):
        pass

    def add_right(self):
        pass

    def delete(self):
        pass

    def attach(self):
        pass