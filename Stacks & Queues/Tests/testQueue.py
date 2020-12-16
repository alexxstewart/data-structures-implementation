import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import Queue

q = Queue.Queue()
q.enqueue(3)
q.enqueue(6)
q.enqueue(10)
print(q.first())
q.dequeue()
q.dequeue()
print(q.first())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)

q.printList()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()

q.printList()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

q.printList()

q.enqueue(13)
q.enqueue(14)
q.enqueue(15)
q.enqueue(16)
q.enqueue(17)
q.enqueue(18)
q.enqueue(19)

q.printList()

