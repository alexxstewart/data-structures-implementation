class Empty(Exception):
    '''linked list is empty'''
    pass

class SinglyLinkedStack:

    class Node:
        def __init__(self, value, next=None):
            self._value = value
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    # this method adds a new element to the front of the linked list
    def push(self, value):
        self._size += 1
        if self._head is None:
            self._head = self.Node(value)
        else:
            # add the new node to the front
            self._head = self.Node(value, self._head)

    # this method removes the first element from the list
    def pop(self):
        self._size -= 1
        if self._head is None:
            raise(self.Empty('Empty list'))
        else:
            self._head = self._head._next

    # this method displays the top element of the stack
    def top(self):
        if self._head is None:
            raise(Empty('Empty list'))
        return self._head._value

    # this method returns the size of the stack
    def size(self):
        return self._size

    def printStack(self):
        if self._head is None:
            raise(self.Empty('Empty list'))
        else:
            currentNode = self._head
            while currentNode is not None:
                print(currentNode._value)
                currentNode = currentNode._next        