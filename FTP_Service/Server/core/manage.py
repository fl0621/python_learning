#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

print('management..........')

from core import main


class ManagementTool():

    def __init__(self, sys_argv):
        self.sys_argv = sys_argv
        self.verify_cmd()

    def verify_cmd(self):
        if len(self.sys_argv) < 2:
            self.help_msg()

    def help_msg(self):
        msg = """
        start   start server
        stop
        restart
        createuser
        """
        exit(msg)

    def execute(self):
        pass

    def start(self):
        server = main.FTPServer(self)
        server.run_forever()
