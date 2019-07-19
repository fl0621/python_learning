#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'


class A:
    __x = 11  # _A__x=11

    def __init__(self, name):
        self.__name = name  # self._A__name

    def __foo(self):  # _A__foo(self)
        print('run foo')

    def bar(self):
        print('run bar')
        self.__foo()  # actually it will execute self._A__foo()


print(A.__dict__)
a = A('denny')

print(a.__dict__)
print(a._A__name)

A.__t1 = 111
a.__t2 = 222
print(A.__dict__)
print(a.__dict__)

a.bar()
