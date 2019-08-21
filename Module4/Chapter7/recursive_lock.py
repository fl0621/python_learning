#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

from threading import Thread, Lock, current_thread, RLock
import time

mutexA = RLock()
mutexB = mutexA
# mutexA = Lock()
# mutexB = Lock()


def func():
    mutexA.acquire()
    print('%s got Lock A' % current_thread().name)
    mutexB.acquire()
    print('%s got Lock B' % current_thread().name)
    mutexA.release()
    time.sleep(0.5)
    mutexA.acquire()
    print('%s got Lock A' % current_thread().name)
    mutexB.release()
    mutexA.release()


t1 = Thread(target=func, )
t2 = Thread(target=func, )
t3 = Thread(target=func, )

t1.start()
t2.start()
t3.start()
