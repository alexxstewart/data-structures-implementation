import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import DoublyLinkedList as DLL

x = DLL.DoublyLinkedList()
x.addToStart(13)
x.addToEnd(47)
x.addToEnd(19)
x.addToStart(98)
x.printListForwards()
print("---------------")
x.printListBackwards()

print("================")

y = DLL.DoublyLinkedList()
y.addToStart(21)
y.addToStart(34)
y.addToStart(87)
y.addToStart(8)
y.addToEnd(43)
y.printListBackwards()
print("---------------")
y.printListForwards()
print("---------------")
y.deleteEnd()
y.deleteStart()
y.printListForwards()
y.deleteEnd()
print('----------------')
y.printListBackwards()
