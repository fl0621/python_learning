# # -*- coding: utf-8 -*-
__author__ = 'Denny'

print('hello word')
count=0
while count <= 100:
    if count == 50:
        pass
    elif count >=60 and count <=80:
        print('loop',count*count)
    else:
        count%2 == 0
        print('loop',count)
    count +=1
print('-------End--------')
