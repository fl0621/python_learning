#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

from socket import *

client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('>>: ').strip()
    client.sendto(msg.encode('utf-8'), ('127.0.0.1', 8081))

    recv = client.recvfrom(1024)
    print(recv[0].decode('utf-8'))

    if msg == 'q':
        break

client.close()
