class Empty(Exception):
    """Error: Attempting to access an element from an empty container"""
    pass

# LIFO stack implemtation using a list as storage.
class Stack:

    def __init__(self):
        self._list = []

    def push(self, value):
        self._list.append(value)
    
    # method removes the last element from the stack
    def pop(self):
        if not self.is_empty():
            self._list.pop()
        else: raise(Empty('Stack is empty'))

    def showTop(self):
        if not self.is_empty():
            print(self._list[-1])
        else: raise(Empty('Stack is empty'))

    def is_empty(self):
        return len(self._list) == 0