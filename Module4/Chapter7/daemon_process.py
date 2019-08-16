#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

from multiprocessing import Process
import time


def task(name):
    time.sleep(2)
    print('%s is running' % name)


if __name__ == '__main__':
    p = Process(target=task, args=('sub 1',))
    p.daemon = True
    p.start()

    print('main process')
