import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import Stack

s = Stack.Stack()

s.push(4)
s.push(3)
s.push(2)
s.showTop()
s.pop()
s.showTop()
print(s.is_empty())
s.pop()
s.showTop()
s.pop()
s.showTop()
