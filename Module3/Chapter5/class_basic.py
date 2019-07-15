#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'


class test():
    a = 'test111'
    count = 0
    def __init__(self):
        self.b2=3

    # print(a)
    # def __init__(self):
    #     self.atrb1 = 'atb111'
    #     self.a = 'from obj'
    #     a = 333
    #     test.count = test.count + 1

    def tt3(self):
        b = 'tt3'
        # print(b)
        print(dir())

aaa=test()
print(type(aaa))
print(aaa.__dict__)

# print(type(test))
# print(test.__dict__)
#
# obj1 = test()
#
# print(type(obj1))
# print(obj1.__dict__)
# # obj.tt3()
#
#
# print(obj1.a)
# print("###############")
#
# print(type(test.a))
# print(test.a)
#
# test.a = 3333333333333
#
# print(type(obj1.a))
# print(obj1.a)
#
# print(test.a)
