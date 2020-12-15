    # This is pretty much a singly linked list but its tail node stores a reference to the head node

class CircularlyLinkedList:

    class Node:
        def __init__(self, reference=None, value=None):
            self.value = value
            self.reference = reference

    def __init__(self):
        self.headNode = None
        self.tailNode = None

    def printList(self):
        currentNode = self.headNode
        while True:
            if currentNode is self.tailNode:
                print(currentNode.value)
                break
            else:
                print(currentNode.value)
                currentNode = currentNode.reference

    def addToStart(self, value):
        if(self.headNode is not None):
            self.headNode = self.Node(self.headNode, value)

            # we need to reassign the refernce of the tail node to the new head node
            self.pointTailToNewHead()
        else:
            node = self.Node(None, value)
            self.headNode = node
            self.tailNode = node

    def addToEnd(self, value):
        if(self.headNode is None):
            node = self.Node(None, value)
            self.headNode = node
            self.tailNode = node
        else:
            currentNode = self.headNode
            while True:
                if currentNode is self.tailNode:
                    # make the new node point to the start and the old node point to the new node
                    node = self.Node(self.headNode, value)
                    self.tailNode = node
                    currentNode.reference = node
                    break
                else:
                    currentNode = currentNode.reference

    def deleteStart(self):
        self.headNode = self.headNode.reference

        # we need to reassign the refernce of the tail node to the new head node
        self.pointTailToNewHead()


    def deleteEnd(self):
        if self.headNode is not None:
            currentNode = self.headNode
            lastNode = None
            while True:
                if currentNode is self.tailNode:
                    # move the reference of the second to last node to the head node
                    lastNode.reference = self.headNode
                    self.tailNode = lastNode
                    break
                else:
                    lastNode = currentNode
                    currentNode = currentNode.reference

    def pointTailToNewHead(self):
        # we need to reassign the refernce of the tail node to the new head node
        currentNode = self.headNode
        while True:
            if currentNode is self.tailNode:
                # if the current node is empty then we are at the end of the list
                # so point the end back to the start
                currentNode.reference = self.headNode
                break
            else:
                currentNode = currentNode.reference
