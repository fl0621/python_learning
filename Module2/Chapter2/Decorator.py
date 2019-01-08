# -*- coding: utf-8 -*-
__author__ = 'Denny'
user_status = False


def login(func):  # henan
    print('login',func)

    def inner(*args,**kwargs):
        _username = "denny"
        _password = "abc123"
        global user_status

        if user_status == False:

            username = input("user:").strip()
            password = input("pasword:").strip()

            if username == _username and password == _password:
                print("welcome login....")
                user_status = True
            else:
                print("wrong username or password!")
        else:
            print("Login Permitted !")

        if user_status:
            func(*args,**kwargs)  # henan()

    return inner


def home():
    print("---首页----")


def america():
    print("----欧美专区----")


@login  # inner
def japan(sj):
    print("----日韩专区----",sj)


@login  # henan = login(henan)
def henan(s1,s2):
    print("----河南专区----",s1,s2)


henan('3c','3d')
japan('90')