#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

from threading import Thread, Semaphore, currentThread
from multiprocessing import Process
import time, random

sm = Semaphore(3)


def task():
    with sm:
        print('%s: %s is using' % (time.time(), currentThread().name))
        time.sleep((random.randint(1, 3)))


if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=task)
        t.start()
