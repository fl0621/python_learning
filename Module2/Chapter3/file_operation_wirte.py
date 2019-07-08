# -*- coding: utf-8 -*-
__author__ = 'Denny'

# file = open("file_operation_write.txt", "w",encoding='utf-8')
#modle：r：read only; w: write only; a: append; r+:read and write
file = open("file_operation_write.txt", "r+",encoding='utf-8')
print(file.read())
file.write("\ntesthgr")
# file.flush()
# 主动将内存写到硬盘，否则写入将发生在缓冲区满或者文件关闭时
print(file.tell())
file.seek(0)
#read以字符为单位，tell，seek为字节
print('22',file.read())
file.close()