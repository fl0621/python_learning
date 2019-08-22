#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

from threading import Timer


def task(name):
    print('timer %s running' % name)


t = Timer(3, task, args=('test1',))
t.start()
print('main finished')
