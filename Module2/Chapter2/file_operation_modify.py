# -*- coding: utf-8 -*-
__author__ = 'Denny'

import os
f_name = "file_operation_modify.txt"
f = open(f_name,"r")
f_new_name = "%s.new" %f_name
f_new = open(f_new_name,"w")
old_str = '1'
new_str = '9'

for line in f:
    if old_str in line:
        line = line.replace(old_str,new_str)
    f_new.write(line)
f.close()
f_new.close()
os.rename(f_new_name,f_name) #windows 中无法覆盖