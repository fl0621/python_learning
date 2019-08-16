# -*- coding: utf-8 -*-
__author__ = 'Denny'

#一层一层进入，再一层一层退出
def calc(n):
    n = int(n/2)
    print(n)
    if n > 0:
        calc(n)
    print(n)

calc(10)

#从最里层返回值到最外层
def r_calc(n,i):
    print(n,i)
    if i < 5:
        return (r_calc(n/2,i+1))
    print(n,i)
    return n

# res = r_calc(188,1)
# print("result",res)
