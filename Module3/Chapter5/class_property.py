#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'


class People:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    @property
    def bmi(self):
        print('#######')
        return self.weight / (self.height ** 2)

    @bmi.setter
    def bmi(self, a1):
        print(a1)


p = People('denny', 65, 1.7)
print(p.bmi)
