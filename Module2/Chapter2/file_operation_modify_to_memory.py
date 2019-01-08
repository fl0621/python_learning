# -*- coding: utf-8 -*-
__author__ = 'Denny'

f_name = "file_operation_modify.txt"
f_obj = open(f_name,"r+")
content = f_obj.read()
f_obj.truncate(0)
old_str = '1'
new_str = 'A'

for line in content:
    if old_str in line:
        line = line.replace(old_str,new_str)
    f_obj.write(line)
f_obj.close()