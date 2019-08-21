#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

from threading import Thread, Event
import time

ev = Event()


def student(name):
    print('student %s is learning' % name)
    ev.wait(2)  # By default thread will be blocked until event.isSet()==True.
    # if timeout time was set thread will become unblocked after 'n' seconds.
    print('student %s is playing' % name)


def teacher(name):
    print('teacher %s is teaching' % name)
    time.sleep(7)
    ev.set()


if __name__ == '__main__':
    stu1 = Thread(target=student, args=('stu1',))
    stu2 = Thread(target=student, args=('stu2',))
    stu3 = Thread(target=student, args=('stu3',))
    t1 = Thread(target=teacher, args=('teacher Cang',))

    stu1.start()
    stu2.start()
    stu3.start()
    t1.start()
