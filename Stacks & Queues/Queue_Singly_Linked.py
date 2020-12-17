class Empty(Exception):
    '''List empty'''
    pass

class SinglyLinkedQueue:
    
    class Node:
        def __init__(self, value, next):
            self._value = value
            self._next = next
    
    def __init__(self):
        self._head = None
        self._tail = None

    def _is_empty(self):
        if self._head is None:
            return True
        return False
    
    # this method adds a value to the end of the linked list
    def enqueue(self, value):
        newNode = self.Node(value, None)
        # if the head is none we make it the head and the tail
        if self._head is None:
            self._head = newNode
            self._tail = newNode
        else:
            # if the head and the tail are the same then we make the new tail and make the head reference it
            if self._head == self._tail:
                self._head._next = newNode
                self._tail = newNode
            else:    
                # we just add the new node to the tail element
                self._tail._next = newNode
                self._tail = newNode

    # this element returns the first element from the linked list
    def dequeue(self):
        if not self._is_empty():
            # get the element and move the head reference along
            element = self._head
            self._head = element._next
            return element
        else:
            raise(self.Empty('Empty list'))

    # this method prints the first element in the queue
    def frist(self):
        if not self._is_empty():
            return self._head._value
    
    # this method prints the queue from the first element to the last
    def printQueue(self):
        if not self._is_empty():
            element = self._head
            while element is not None:
                print(element._value)
                element = element._next
        else:
            raise(self.Empty('Empty list'))