import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import Dequeue

d = Dequeue.Dequeue()

d.add_to_front(1)
d.add_to_end(2)
d.add_to_front(0)
d.add_to_end(3)
d.add_to_end(4)
d.add_to_front(-1)
d.printList()
d.add_to_end(5)
d.add_to_front(-2)
d.add_to_front(-3)
d.add_to_front(-4)
d.printList()
d.add_to_front(-5)
d.printList()
d.remove_first()
d.printList()
d.remove_last()
d.printList()

d.remove_last()
d.remove_first()
d.remove_first()
d.printList()