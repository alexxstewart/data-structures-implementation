import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import Queue_Singly_Linked

q = Queue_Singly_Linked.Singly_Linked_Queue()
q.enqueue(0)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.printQueue()
print('--------------------------------------')
q.dequeue()
q.dequeue()
q.dequeue()
q.printQueue()