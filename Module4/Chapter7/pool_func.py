#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threading import currentThread
import os, time, random


def task(name):
    print('name: %s pid:%s is running,name: %s' % (name, os.getpid(), currentThread().name))
    time.sleep(random.randint(1, 3))


if __name__ == '__main__':

    # pool = ThreadPoolExecutor(3)
    pool = ProcessPoolExecutor(3)

    for i in range(10):
        pool.submit(task, i)

    pool.shutdown()
    # pool.map()

    print('main')
