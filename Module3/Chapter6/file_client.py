#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'
import socket, struct, json

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    c.connect(('127.0.0.1', 6161))

    while True:
        send_data = input(':>>')
        if not send_data.strip():
            print('input cant be empty ', send_data)
            continue
        c.send(send_data.strip().encode('utf-8'))

        struct_obj = c.recv(4)
        header_size = struct.unpack('i', struct_obj)[0]
        header_bytes = c.recv(header_size)
        header_json = header_bytes.decode('utf-8')
        header_dic = json.loads(header_json)
        print(header_dic)
        total_size = header_dic['file_size']
        filename = header_dic['file_size']

        with open('c.txt', 'wb') as f:  # filename
            recv_size = 0

            while recv_size < total_size:
                line = c.recv(1024)
                f.write(line)
                recv_size += len(line)

except Exception as e:
    print('errorrrrrrr', e)
finally:
    c.close()
