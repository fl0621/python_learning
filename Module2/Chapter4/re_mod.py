#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

# import re
#
# f = open("contacts.txt")
# data = f.read()
#
# result = re.findall("[0-9]{11}", data)
#
# print(result)
#
# f.close()


import re

s = "51032120denny0804050175"
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{3})', s)
print(res.groupdict())

print(s)
print(re.sub('\d+', '$', s))
