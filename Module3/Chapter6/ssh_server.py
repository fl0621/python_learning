#!/usr/bin/env python3
# coding: utf-8
__author__ = 'Denny'
import socket, subprocess, struct, json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # ip,port reuse
s.bind(('127.0.0.1', 6161))
s.listen(5)  # the number of waiting queue
# s.setblocking(False)  # set socket server to non-blocking model
print('starting......')

while True:
    conn, client_addr = s.accept()  # call s.accept() will return a tuple
    print(conn)
    print(client_addr)
    while True:
        try:
            data = conn.recv(1024)  # max size of data can be receive in one time in bytes.
            if not bytes.decode(data):
                break
            print('received data: ', bytes.decode(data))
            if bytes.decode(data) == 'q':
                print('exiting from client')
                conn.close()
                s.close()
                exit(1)
                # break
            obj = subprocess.Popen(data.decode('utf-8'), shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            header_dic = {
                'filename': 'a.text',
                'md5': 'test512356',
                'total_size': len(stdout) + len(stderr)
            }
            header_json = json.dumps(header_dic)
            header_bytes = header_json.encode('utf-8')  # bytes to string
            print('data size: ', header_dic['total_size'])
            # below code will pack a specify type of data to bytes type,
            # the length will be 4 bytes,
            # if data length is not enough '0' will be filled in.
            conn.send(struct.pack('i', len(header_bytes)))

            conn.send(header_bytes)
            conn.send(stdout + stderr)
        except ConnectionResetError as e:  # for windows
            print('error', e)
    conn.close()
