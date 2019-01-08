# -*- coding: utf-8 -*-
__author__ = 'Denny'

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{
            '浦东机场':{}
        },
    },
    '山东':{},
}
CurrentDict = menu  #当前所在字典
HigherDict = None
# print(CurrentDict)
CurrentKeyList = list(CurrentDict.keys())  #当前字典的key的列表
# print(CurrentKeyList)
Banner = '********Select Location*********'
print(Banner)
i=0
while i < len(CurrentKeyList):
    print(i,' : ',CurrentKeyList[i])
    i += 1
    while i == len(CurrentKeyList):
        print('\n')
        print('Input "q" for Quit,')
        print('Input "b" for Return.')
        choice =input('please input your choice:')
        # print(choice)
        if choice == 'q':    #输入q则退出
            print('User Exit!!')
            exit(0)
        elif choice == 'b':  #输入b则返回，只能向上返回一级，无法返回多级
            if HigherDict == None:
                print("you already at the top level! ")
            else:
                CurrentDict = HigherDict.copy()  #通过调整当前字典来调整层级
                # print(CurrentDict)
                CurrentKeyList = list(CurrentDict.keys())
                # print(CurrentKeyList)
            print(Banner)
            i = 0
        elif choice.isdigit():
            choice = int(choice)
            if CurrentDict.get(CurrentKeyList[choice]) == None:
                print('Selection not found')
            else:
                # print (CurrentKeyList[choice])
                HigherDict = CurrentDict.copy()
                CurrentDict = CurrentDict.get(CurrentKeyList[choice])
                # print(CurrentDict)
                CurrentKeyList = list(CurrentDict.keys())
                # print(CurrentKeyList)
                i = 0
                print(Banner)
        else:
            import os  #如果都不匹配，那么就是输入了错误的选项，
            os.system('cls')
            print('Input error, try again!')
            i = 0  #通过修改i的值来控制程序逻辑