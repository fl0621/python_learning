# -*- coding: utf-8 -*-
__author__ = 'Denny'

menus = [
    {
        'text': '北京',
        'children': [
            {'text': '朝阳', 'children': []},
            {'text': '昌平', 'children': [
                {'text': '沙河', 'children': []},
                {'text': '回龙观', 'children': [
                    {'text': '回龙幼儿园', 'children': []}
                ]},
            ]},
        ]
    },
    {
        'text': '上海',
        'children': [
            {'text': '宝山', 'children': []},
            {'text': '金山', 'children': []},
            {'text': '浦东', 'children': [
                {'text': '浦东机场', 'children': [
                    {'text': '国际达到', 'children': []}
                ]}
            ]},
        ]
    }
]
def print_node (current_list):
    lengh =len(current_list)
    i=0
    while i < lengh:
        print(current_list[i]['text'])
        if (len(current_list[i]['children'])) == 0:
            pass
        else:
            uperlist = current_list.copy()
            current_list = current_list[i]['children']
            print_node(current_list)
            current_list = uperlist.copy()
        i += 1

print_node(menus)

def find_node (node_name,current_list):
    lengh =len(current_list)
    i=0
    while i < lengh:
        if (current_list[i]['text']) == node_name:
            print(node_name)
            return True
        if (len(current_list[i]['children'])) == 0:
            pass
        else:
            uperlist = current_list.copy()
            current_list = current_list[i]['children']
            feedback = find_node(node_name,current_list)
            if feedback == True:
                print(node_name)
                # print(feedback)
                return feedback
            else:
                current_list = uperlist.copy()
        i += 1


location =input('输入个地名:').strip()
print(find_node(location,menus))

#1. 打印所有的节点
#2. 输入一个节点名字，沙河， 你要遍历找，找到了，就打印它，并返回true,