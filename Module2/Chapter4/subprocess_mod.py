#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

import subprocess, signal

# standard usage, if set 'check' to 'True' and the exit code was non-zero, it raises a CalledProcessError.
# r = subprocess.run(['df', '-hT'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
# if your command have a pipe operator make sure set 'shell' parameter to 'True' and don't use subprocess.PIPE anymore.
# r2 = subprocess.run('df -hT | grep sda', shell=True)


# a = subprocess.run('sleep 3 ', shell=True, stdout=subprocess.PIPE)
print('hgh#########')

obj = subprocess.Popen('sleep 3 ', shell=True, stdout=subprocess.PIPE)

# obj.poll()
# obj.wait()
# obj.terminate()
# obj.kill()
# obj.communicate() #only one time

print(obj)

# obj.send_signal(signal.SIGKILL)
print(dir(obj))
