#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

from gevent import monkey;monkey.patch_all()
import gevent, time


def eat(name):
    print('%s eat 1' % name)
    time.sleep(3)
    print('%s eat 2' % name)


def play(name):
    print('%s play 1' % name)
    time.sleep(4)
    print('%s play 2' % name)


start_time = time.time()
g1 = gevent.spawn(eat, 'denny')
g2 = gevent.spawn(play, 'king')
# g1.join()
# g2.join()
gevent.joinall((g1, g2))
stop_time = time.time()
print(stop_time - start_time)
