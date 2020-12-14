class DoublyLinkedList:
    
    class Node:
        def __init__(self, forwardReference=None, backwardReference=None , value=None):
            self.value = value
            self.forwardReference = forwardReference
            self.backwardReference = backwardReference

    def __init__(self):
        self.headNode = None

    def printListForwards(self):
        currentNode = self.headNode
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.forwardReference

    def printListBackwards(self):
        currentNode = self.headNode
        while True:
            if currentNode.forwardReference is not None:
                currentNode = currentNode.forwardReference
            else:
                break
        
        # we now have the last node so we can just print it backwards by using the backwards references
        while True:
            if currentNode is not None:
                # print node
                print(currentNode.value)
                currentNode = currentNode.backwardReference
            else:
                break

    def addToStart(self, value):
        if(self.headNode is not None):
            newNode = self.Node(self.headNode, None, value)
            self.headNode.backwardReference = newNode
            self.headNode = newNode
        else:
            self.headNode = self.Node(None, None, value)

    def addToEnd(self, value):
        if(self.headNode is None):
            self.headNode = self.Node(None, None, value)
        else:
            currentNode = self.headNode
            lastNode = None
            while True:
                if currentNode is None:
                    node = self.Node(None, lastNode, value)
                    lastNode.forwardReference = node
                    break
                else:
                    lastNode = currentNode
                    currentNode = currentNode.forwardReference

    def deleteStart(self):
        if self.headNode is not None:
            self.headNode = self.headNode.forwardReference
            self.headNode.backwardReference = None

    def deleteEnd(self):
        if self.headNode is not None:
            currentNode = self.headNode
            lastNode = None
            while True:
                if currentNode.forwardReference is None:
                    lastNode.forwardReference = None
                    break
                else:
                    lastNode = currentNode
                    currentNode = currentNode.forwardReference