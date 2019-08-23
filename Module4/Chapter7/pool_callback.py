#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threading import currentThread
import os, time, random


def task(name):
    print('name: %s pid:%s is running,name: %s' % (name, os.getpid(), currentThread().name))
    time.sleep(random.randint(3, 5))
    t = time.time()
    return t


def show(t_time):
    print(t_time.result())


if __name__ == '__main__':

    # pool = ThreadPoolExecutor(3)
    pool = ProcessPoolExecutor(3)

    for i in range(5):
        pool.submit(task, i).add_done_callback(show)

    # pool.shutdown()
    # pool.map()
    print('main')
