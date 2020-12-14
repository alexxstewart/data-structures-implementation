class LinkedList:

    class Node:
        def __init__(self, reference=None, value=None):
            self.value = value
            self.reference = reference

    def __init__(self):
        self.headNode = None

    def printList(self):
        currentNode = self.headNode
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.reference

    def addToStart(self, value):
        if(self.headNode is not None):
            self.headNode = self.Node(self.headNode, value)
        else:
            self.headNode = self.Node(None, value)

    def addToEnd(self, value):
        if(self.headNode is None):
            self.headNode = self.Node(None, value)
        else:
            currentNode = self.headNode
            lastNode = None
            while True:
                if currentNode is None:
                    node = self.Node(None, value)
                    lastNode.reference = node
                    break
                else:
                    lastNode = currentNode
                    currentNode = currentNode.reference