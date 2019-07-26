#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'
import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    c.connect(('127.0.0.1', 6161))

    while True:
        send_data = input(':>>')
        if not send_data.strip():
            print('input cant be empty ', send_data)
            continue
        c.send(send_data.strip().encode('utf-8'))
        data = c.recv(1024)
        print(data.decode('utf-8'))
except Exception as e:
    print('errorrrrrrr', e)
finally:
    c.close()
