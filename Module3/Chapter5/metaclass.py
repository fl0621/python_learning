#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

# a = "print ('ttttest')"
# exec(a)
#
#
# class Foo:
#     pass
#
#
# obj = Foo()
#
# print(type(obj))
# print(type(Foo))

class_name = 'chinese'
class_bases = (object,)

class_body = """
country='china1'

def __init__(self,name,age):
    self.name=name
    self.age=age
    
def talk(self):
    print('%s is talking' %self.name)
"""

class_dic = {}
exec(class_body, globals(), class_dic)
print(class_dic)

chinese = type(class_name, class_bases, class_dic)
print(chinese)
print(type(chinese))

obj = chinese('denny', '18')
print(obj)
print(type(obj))
obj.talk()
