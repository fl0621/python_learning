#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

from multiprocessing import Process
import time
import os


def task(name):
    print('%s: %s:%s is running' % (time.time(), name, os.getpid()))
    time.sleep(10)
    print('%s: %s:%s is done' % (time.time(), name, os.getpid()))


if __name__ == '__main__':
    p1 = Process(target=task, args=('first process',), name='proce-1')
    p2 = Process(target=task, args=('second process',))
    p3 = Process(target=task, args=('third process',))

    p1.start()  # only OS can open a new process, what python done was send a request to OS.
    p2.start()
    p3.start()

    # in python3 map() function return an iterator, in python2 return a list.
    # p_list = (p1, p2, p3)
    # res = map(Process.start, p_list)
    # print(list(res))

    print('p1 is alive: ', p1.is_alive())
    time.sleep(1)
    p1.terminate()  # ask OS to terminate process 'p1'
    time.sleep(1)
    p1.join()  # at current position join() will block main process until p1 process finished.
    print('p1 is alive: ', p1.is_alive())

    print('p1 name is: ', p1.name)

    print('%s: main\'s pid:%s, ppid:%s' % (time.time(), os.getpid(), os.getppid()))
