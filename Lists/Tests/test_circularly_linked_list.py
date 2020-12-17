import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import CirularlyLinkedList as CLL

x = CLL.CircularlyLinkedList()
x.addToStart(1)
x.addToStart(0)
x.addToStart(32)
x.addToEnd(43)
x.deleteStart()
x.deleteEnd()
x.printList()

print('--------------')

y = CLL.CircularlyLinkedList()
y.addToEnd(40)
y.addToEnd(50)
y.addToEnd(60)
y.addToEnd(70)
y.addToEnd(80)
y.addToEnd(90)
y.addToEnd(100)
y.deleteStart()
y.deleteStart()
y.printList()