#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'
import socket, os, struct, json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # ip,port reuse
s.bind(('127.0.0.1', 6161))
s.listen(5)
print('starting......')

while True:
    conn, client_addr = s.accept()
    print(conn)
    print(client_addr)
    while True:
        try:
            data = conn.recv(1024)  # max size of data can be receive in one time in bytes.
            if not bytes.decode(data): break
            print('received data: ', bytes.decode(data))
            if bytes.decode(data) == 'q':
                print('exiting from client')
                exit(1)
                # break
            cmd = data.decode('utf-8').split()
            filename = cmd[1]

            header_dic = {
                'filename': filename,
                'md5': 'test512356',
                'file_size': os.path.getsize(filename)
            }
            header_json = json.dumps(header_dic)
            header_bytes = header_json.encode('utf-8')

            print('data size: ', header_dic['file_size'])
            conn.send(struct.pack('i', len(header_bytes)))
            conn.send(header_bytes)

            with open(filename, 'rb') as f:
                for line in f:
                    conn.send(line)
        except ConnectionResetError as e:  # for windows
            print('error', e)
    conn.close()
s.close()
