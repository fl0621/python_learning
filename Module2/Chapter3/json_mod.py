#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

import json

data = {
    'roles': [
        {'role': 'monster', 'type': 'pig', 'life': 50},
        {'role': 'hero', 'type': 'guanyu', 'life': 81}
    ]
}

d = json.dumps(data)  # serialization dict to str
print(type(d), d)

d2 = json.loads(d)  # deserialization str to dict

print(type(d2), d2)

with open('test.json', 'w') as f:
    json.dump(data, f)  # serialization dict to str and write to file

with open('test.json', 'r') as f:
    t = json.load(f)  # read from file and deserialization str to dict
    print(type(t), t)
# json.dump and json.load only accept a file object don't use file name directly.
