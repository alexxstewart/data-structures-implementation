import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import LinkedList

x = LinkedList.LinkedList()
x.addToStart(3)
x.addToStart(4)
x.addToEnd(243)
x.addToStart(7)
x.addToEnd(14)
x.addToStart(0)
x.addToStart(7896)
x.addToEnd(165943)
x.deleteStart()
x.deleteEnd()
x.printList()

print('=============')

y = LinkedList.LinkedList()
y.addToEnd(4)
y.addToEnd(5)
y.addToStart(8)
y.addToEnd(18)
y.printList()

print("=================")

z  = LinkedList.LinkedList()
z.addToStart(4)
z.addToStart(3)
z.addToStart(14)
z.deleteEnd()
z.deleteStart()
z.printList()