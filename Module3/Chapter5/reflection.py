#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print("%s is talking " % self.name)


obj = People('denny', 20)

print('has', hasattr(obj, 'name'))
print('get', getattr(obj, 'talk'))
print('set', setattr(obj, 'gender', 'male'))
print('get2', getattr(obj, 'gender'))

delattr(obj, 'gender')
print('has2', hasattr(obj, 'gender'))