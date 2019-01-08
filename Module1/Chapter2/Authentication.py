# -*- coding: utf-8 -*-
__author__ = 'Denny'

f = open('./1.txt','r+')
status = f.read()
if 'locked' in status:
    print('system locked, exit!')
    exit(1)

account = {'user1':'pass1','user2':'pass2'}
i=0
while i < 3:
    while True:
        user = input('input your username:')
        if user == '' :
            print("username can't be empty")
        else:
            break
    passwd = input('input your password:')
    if account.get(user) == None :
        print('username not found')
    elif passwd != account.get(user):
        print('password error')
    else:
        print('welcomme')
        break
    i +=1
    if i == 3:
        f.write('locked')
f.close()