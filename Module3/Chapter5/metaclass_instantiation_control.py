#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'


class MyMeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        print('class name: ', class_name)
        print(class_bases)
        print(class_dic)
        if not class_name.istitle():
            raise TypeError('test exception')
        if not '__doc__' in class_dic or not class_dic['__doc__'].strip():
            raise TypeError('must have comments')
        super().__init__(class_name, class_bases, class_dic)

    def __call__(self, *args, **kwargs):
        # first:create an empty obj
        obj = object.__new__(self)
        # second:initialize obj
        self.__init__(obj, *args, **kwargs)
        print('callllllllllllllll')
        # third:return obj
        return obj


class Chinese(object, metaclass=MyMeta):  # Chinese = MyMeta(class_name, class_bases, class_dic)
    """
    test comments
    """
    country = 'china'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)


obj = Chinese('denny', age=18)
print(obj.__dict__)
