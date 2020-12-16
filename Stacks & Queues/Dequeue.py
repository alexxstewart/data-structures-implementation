class Dequeue:
    class Empty(Exception):
        """Error: Attempting to access an element from an empty container"""
        pass

    DEFAULT_CAPACITY = 10

    def __init__(self):
        # create the list 
        self._list = [None] * self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    # method returns true if the list is empty
    def is_empty(self):
        return len(self._list) == 0

    # this method returns the first element of the queue otherwise throws an exception
    def first(self):
        if self.is_empty():
            raise(Empty('queue is empty'))
        return self._list[self._front]

    # this method returns the last element of the dequeue
    def last(self):
        if self.is_empty():
            raise(Empty('queue is empty'))
        return self._list[(self._front + self._size - 1) % len(self._list)]

    # this method returns and deletes the first element from the queue
    def remove_first(self):
        # first we check if the list is empty
        if self.is_empty():
            raise(Empty('queue is empty'))
        
        # get the element at the front of the queue and set its position to none
        element = self._list[self._front]
        self._list[self._front] = None

        # calculate the new size and front position for the list
        self._size -= 1
        self._front = (self._front + 1) % len(self._list)

        return element

    # this method adds a specified element to the end of the queue
    def add_to_end(self, value):
        # first we check if the list is full
        if self._size == len(self._list):
            self.resize()
        
        if self._size == 0:
            pos = 0
        else:
            pos = (self._size + self._front) % len(self._list)
        
        self._list[pos] = value
        self._size += 1

    def add_to_front(self, value):
        if self._size == len(self._list):
            self.resize()
        
        if self._size == 0:
            pos = 0
        else:
            pos = (self._front - 1) % len(self._list)
        self._list[pos] = value
        self._front = pos
        self._size += 1

    # this method removes the last element of the dequeue
    def remove_last(self):
        if self.is_empty():
            raise(Empty('list is empty'))
        self._size -= 1
        pos = (self._front + self._size) % len(self._list)
        self._list[pos] = None

    # this method handles resizing the list when there are too many elements in the list
    def resize(self):
        old = self._list
        newSize = len(old) * 2
        self._list = [None] * newSize

        # now we assign the old elements into the new list
        pos = self._front
        for i in range(self._size):
            self._list[i] = old[pos]
            pos = (1 + pos) % len(old)

        print(self._list)

        # move the front index to 0
        self._front = 0

    def printList(self):
        print(self._list)