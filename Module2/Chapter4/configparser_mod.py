#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

import configparser

conf = configparser.ConfigParser()
conf.read("conf.ini")

print(conf.sections())
print(conf['bitbucket.org']['ServerAliveInterval'])
# conf.set()
