# -*- coding: utf-8 -*-
__author__ = 'Denny'


def fib(max):
    n, a, b = 0, 1, 1
    while n < max:
        print('before yield')
        sent = yield b        # 把b的值返回给next并暂停函数的执行
        if sent == 'stop':    # 再次调用next，函数将从上次的地方继续执行
            print('---',sent)
            break
        a, b = b, a + b
        n = n + 1
    return 'Done'


f = fib(16)  # 直接调用函数，函数将不会执行
print(f)     # 只是返回一个生成器对象
print("*****")
print(next(f))
#print(f.__next__())
print(next(f))
# next(f)
f.send('stop')
