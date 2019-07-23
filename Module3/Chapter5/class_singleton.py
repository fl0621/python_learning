#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'


class Mysql:
    __instance = None

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306

    @classmethod
    def singleton(cls):
        if not cls.__instance:
            obj = cls()
            cls.__instance = obj
        return cls.__instance

    def conn(self):
        pass

    def execute(self):
        pass


obj1 = Mysql.singleton()
obj2 = Mysql.singleton()
print(obj1)
print(obj2)
