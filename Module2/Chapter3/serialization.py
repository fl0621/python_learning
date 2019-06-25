#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

#
# data = {
#     'roles': [
#         {'role': 'monster', 'type': 'pig', 'life': 50},
#         {'role': 'hero', 'type': 'guanyu', 'life': 80}
#     ]
# }
#
# print(data)
#
# with open("game_status.txt", 'w') as f:
#     f.write(str(data))

with open("game_status.txt", 'r') as f:
    t = f.read()
print(eval(t)['roles'][0]['role'])
