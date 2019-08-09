#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'
import os

HOST = '127.0.0.1'
PORT = 6666

Base_dir = os.path.dirname(os.path.dirname(__file__))
HOME_DIR = os.path.join(Base_dir, 'home')
DB_DIR = ''
ACCOUNT_FILE = '%s/conf/accounts.ini' % Base_dir

print(dir())
