#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'


class Foo:

    def __init__(self, name):
        self.name = name

    def output(self):
        print("name is %s" % self.name)

    @classmethod
    def func1(cls):
        print(cls)
        print('class method name %s' % cls.__name__)

    @staticmethod
    def func2():
        print('static method')


obj = Foo('denny')

obj.func1()
Foo.func1()

obj.func2()
Foo.func2()
