#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'

from socket import *

server = socket(AF_INET, SOCK_DGRAM)
server.bind(('127.0.0.1', 8081))

while True:

    recv = server.recvfrom(1024)
    print(recv)
    data, client_addr = recv
    server.sendto(data.upper(), client_addr)
    if data == 'q':
        break

server.close()
