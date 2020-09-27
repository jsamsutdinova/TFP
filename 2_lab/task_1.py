#!/usr/bin/env python3
""" Laboratory work 2. Task 1 """

from stack.stack import Stack

s = Stack([5,7, 4, 9, 1, 6, 2])

print(s.push())
print("Deleted item from Stack:", s.pop())
print("Last item in Stack:", s.back())
print("Size of stack:", s.size())
print(s.clear())
print("Bye!")
