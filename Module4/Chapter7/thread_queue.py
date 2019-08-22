#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

import queue

q = queue.Queue(3)  # queue, first in  first out
for i in range(3):
    q.put(i)
for i in range(3):
    print(q.get())

q2 = queue.LifoQueue(3)  # stack, last in first out
for i in range(3):
    q2.put(i)
for i in range(3):
    print(q2.get())

q3 = queue.PriorityQueue(5)  # priority queue, smaller number have a higher priority.
q3.put((7, 'fdaa'))
q3.put((4, 'bzzb'))
q3.put((5, '11bzzb'))

print(q3.get())
print(q3.get())
print(q3.get())
