# -*- coding: utf-8 -*-
__author__ = 'Denny'
goods =[
{"name":"电脑", "price": 1999},
{"name":"鼠标", "price": 10},
{"name":"游艇", "price": 20},
{"name":"宝剑", "price": 998},
]
user = 'uuu'
passwd = 'ppp'
user_input = input('input your usernmae:')
while user_input == '':
    print("username can't be empty")
    user_input = input('input your usernmae again:')
else:
    if not user_input == '':
        pass_input = input('input your passcode:')
        if user_input == user and pass_input == passwd:
            print('how much is your salary?')
            salary = input('my salary is :')
            while not salary.isdigit():
                print('please input a digit,')
                salary = input('try again:')
            else:
                salary = int(salary)
                print(salary)
                ProductsID = 0
                balance = salary
                cart = []
                while ProductsID < len(goods):
                    # print('products',ProductsID)
                    print(ProductsID,': ',goods[ProductsID].get('name'),'→',goods[ProductsID].get('price'))
                    ProductsID += 1
                    while  ProductsID == len(goods):
                        print('what products do you want?')
                        print('Input "q" for exit!')
                        buy = input('input product ID:')
                        if buy == 'q':
                            print('---you have below products in your shopping cart---')
                            print(cart)
                            print('your balance is','\033[1;31;43m',balance,'\033[0m')
                            exit()
                        elif buy.isdigit():
                            buy = int(buy)
                            ProductPrice = goods[buy].get('price')
                            if balance >= ProductPrice:
                                balance -= ProductPrice
                                cart.append(goods[buy].get('name'))
                                print('you have added ','\033[1;31;43m',goods[buy].get('name'),'\033[0m','to your cart')
                                print('you still have','\033[1;31;43m',balance,'\033[0m','in your wallet')
                            else:
                                print('you only have', '\033[1;31;43m', balance, '\033[0m', 'in your wallet')
                                print('please select a cheaper one')
                        else:
                            print('input not correct')
                        ProductsID = 0
        else:
            print('username or password error')
            print('Login failure \033[0m  ,Bye!!')