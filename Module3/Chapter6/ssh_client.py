#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'
import socket, struct, json

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    c.connect(('127.0.0.1', 6161))

    while True:
        send_data = input(':>> ')
        if not send_data.strip():
            continue
        c.send(send_data.strip().encode('utf-8'))

        struct_obj = c.recv(4)
        header_size = struct.unpack('i', struct_obj)[0]
        header_bytes = c.recv(header_size)
        header_json = header_bytes.decode('utf-8')
        header_dic = json.loads(header_json)
        print(header_dic)
        data_size = header_dic['total_size']

        recv_size = 0
        recv_data = b''
        print(type(recv_data))

        while recv_size < data_size:
            data = c.recv(1024)
            recv_data += data
            recv_size += len(data)

        print(recv_data.decode('utf-8'))
except Exception as e:
    print('errorrrrrrr', e)
finally:
    c.close()
