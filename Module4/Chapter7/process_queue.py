#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

from multiprocessing import Process, Queue
import time


# q = Queue(3)
#
# q.put('hello')
# q.put({'a': 1, 'b': 2})
# q.put([1, 2, 3, 4])
#
# print(q.full())
# print(q.get())
# q.put(4)
#
# print(q.qsize())
# print(q.empty())  # not reliable

def producer(q):
    for i in range(10):
        res = 'baozi %s' % i
        time.sleep(0.25)
        print('%s , producted' % res)
        q.put(res)
    else:
        q.put('over')


def consumer(q):
    while 1:
        time.sleep(0.5)
        q_data = q.get()
        print('ate %s' % q_data)
        print(q.qsize())
        if q_data == 'over':
            break


if __name__ == '__main__':
    q = Queue(10)
    p1 = Process(target=producer, args=(q,))
    c1 = Process(target=consumer, args=(q,))
    p1.start()
    c1.start()
    print('main')
