# -*- coding: utf-8 -*-
__author__ = 'Denny'

products = [ ['Iphone8',6888],['MacPro',14800], ['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799] ]
shopping_cart = []
run_flag = True
while run_flag:
    print('---------Products List----------')
    for index,p in enumerate(products):
        print("%s. %s  %s" %(index,p[0],p[1]))
    choice = input("input goods number:")
    if choice.isdigit():
        choice = int(choice)
        if choice >= 0 and choice < len(products):
            shopping_cart.append(products[choice])
            print('Added product %s into shopping cart.' %(products[choice]))
        else:
                print("products doesn't exit")
    elif choice == 'q':
        if len(shopping_cart) >0:
            print('----You have added below products in to cart----')
            for index, p in enumerate(shopping_cart):
                print("%s. %s  %s" % (index, p[0], p[1]))
        run_flag = False
        # break