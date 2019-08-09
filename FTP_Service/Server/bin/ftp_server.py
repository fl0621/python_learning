#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

import os, sys

Base_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, Base_dir)

print(sys.path[0])

if __name__ == "__main__":
    from core import manage

    argv_parser = manage.ManagementTool(sys.argv)
    argv_parser.execute()
    print(manage.ManagementTool.__dict__)
