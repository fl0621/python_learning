#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'


class ParentClass1:
    p1 = 33

    def print_t1(self):
        print("parent1")

    def prt(self):
        print("prt p1")

        super().prt()


class ParentClass2:
    def print_t2(self):
        print("parent2")

    def prt(self):
        print("prt p2")


class SubClass1(ParentClass1):
    # p1 = 55
    print(super.mro())

    def print_t1(self):
        print('modify t1')

    def prt(self):
        print("prt s1")


class SubClass2(ParentClass1, ParentClass2):
    pass


# print(SubClass1.__bases__)
# print(SubClass2.__bases__)

# s1 = SubClass1()
# print(s1.p1)

print(SubClass2.mro())

temp = SubClass2()
temp.prt()

# temp2=SubClass1()