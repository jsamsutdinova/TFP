#!/usr/bin/env python3
""" Laboratory work 2. Task 2 """

import numpy as np
from deque.deque import Deque

d = Deque(np.array([3, 5, 7, 6, 4, 9]))

print(d.push_front())
print(d.push_back())
print("First item is deleted:", d.pop_front())
print("Last item is deleted:", d.pop_back())
print("First item of deque:", d.front())
print("Last item of deque:", d.back())
print("Size of deque:", d.size())
print(d.clear())
