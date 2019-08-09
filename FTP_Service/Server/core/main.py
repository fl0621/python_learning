#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

import socket
from conf import settings
import json, configparser, hashlib


class FTPServer():
    STATUS_CODE = {
        '200': 'success',
        '400': 'fail'
    }

    def __init__(self, manage_instance):
        self.manage_instance = manage_instance
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((settings.HOST, settings.PORT))
        self.accounts = self.load_accounts()

    def run_forever(self):
        print('started')
        self.conn, self.addr = self.sock.accept()
        self.handle()

    def handle(self):
        while 1:
            raw_data = self.conn.recv(1024)
            if not raw_data:
                pass
            data = json.loads(raw_data.decode('utf-8'))
            action_type = data.get('action_type')
            if action_type:
                if hasattr(self, 'c_%s' % action_type):
                    func = getattr(self, 'c_%s' % action_type)
                    func(data)
            else:
                print('invalid command,')

    def load_accounts(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(settings.ACCOUNT_FILE)
        print(config_obj.sections())
        return config_obj

    def authenticate(self, username, password):
        if username in self.accounts:
            c_password = self.accounts[username]['password']
            md5_obj = hashlib.md5()
            md5_obj.update(password.encode('utf-8'))
            if c_password == md5_obj.hexdigest():
                return True
            else:
                print('wrong password')

    def send_response(self, status_code, *args, **kwargs):
        data = kwargs
        data['status_code'] = status_code
        data['status_msg'] = self.STATUS_CODE[status_code]

        bytes_data = json.dumps(data).encode()
        self.conn.send(bytes_data)

    def c_auth(self, data):
        print('auth', data)

        if self.authenticate(data['username'], data['password']):
            print('auth successfully')
            self.send_response(200)
        else:
            self.send_response(201)
