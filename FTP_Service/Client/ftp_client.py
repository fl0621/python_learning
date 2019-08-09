#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

import optparse
import socket
import json


class FTPClient():

    def __init__(self):
        obj = optparse.OptionParser()
        obj.add_option('-s', '--server', dest='IP', help='server ip address')
        obj.add_option('-p', '--port', type='int', dest='port', help='server port')
        obj.add_option('-u', '--user', dest='user', help='input username')
        self.options, self.args = obj.parse_args()
        self.argv_verification()
        self.make_connection()

        print(self.options, self.args)

    def argv_verification(self):
        if not self.options.IP:
            exit('must input server ip')

    def make_connection(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.options.IP, self.options.port))

    def send(self):
        pass

    def interactive(self):
        if self.auth():
            pass

    def auth(self):
        count = 0
        while count < 3:
            username = input('username:').strip()
            if not username:
                continue
            password = input('usepassword:').strip()
            cmd = {
                'action_type': 'auth',
                'username': username,
                'password': password
            }
            self.sock.send(json.dumps(cmd).encode('utf-8'))
            self.sock.recv(1024)


if __name__ == '__main__':
    client = FTPClient()
    client.interactive()
