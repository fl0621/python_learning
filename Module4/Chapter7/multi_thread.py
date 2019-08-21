#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

from threading import Thread,current_thread,enumerate,Event
from multiprocessing import Process

n = 100


def func():
    global n
    n = 666


if __name__ == '__main__':
    t1 = Thread(target=func, )
    t1.start()
    print('n in main, ', n)
    print(t1.name)
    t1.name='b33'
    print('name modified: ',t1.getName())
    print(current_thread().getName())
    print(enumerate())

    ev=Event()

    print(ev.isSet())
