# -*- coding: utf-8 -*-
__author__ = 'Denny'

import chardet  #非默认模块，pip3 install chardet
file = open("file_operation.txt","rb")  #b means binary
data = file.read()  #调用file对象的read方法
result = chardet.detect(data)   #character detector，用以发现字符编码
print(result)
print(data.decode('gb2312'))