#!/usr/bin/python
#coding:utf-8

import socket

s=socket.socket()
s.connect(("127.0.0.1",8888))
f=open('qr.png','wb+')
f.write(s.recv(65535))