#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'


class A:
    __x = 11  # _A__x=11

    def __init__(self, name):
        self.__name = name

    def __foo(self):
        print('run foo')

    def bar(self):
        print(A.__x)


print(A.__dict__)

a = A('denny')
print(a.__dict__)

print(a._A__x)

A.__t1 = 111
a.__t2 = 222
print(A.__dict__)
print(a.__dict__)

a.bar()
