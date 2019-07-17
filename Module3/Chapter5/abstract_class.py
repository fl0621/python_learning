#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

import abc


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass

    def eat(self):
        pass


class People(Animal):
    def run(self):
        print('%s is walking' % self.__class__.__name__)


class Pig(Animal):
    def run(self):
        print('%s is walking' % self.__class__.__name__)


class Dog(Animal):
    def run1(self):
        print('%s is walking' % self.__class__.__name__)


peo1 = People()
pig1 = Pig()
dog1 = Dog()

peo1.run()
pig1.run()

print(type(Animal))
