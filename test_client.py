#!/usr/bin/python3
#coding:utf-8

import socket
import json

s=socket.socket()
s.connect(("127.0.0.1",8888))
f=open('qr.png','wb+')
f.write(s.recv(65535))
f.close()
while(True):
    """
    {
        "type":MSGTYPE,
        "name":USERNAME,
        "text":TEXT,
        "id":ID
    }
    """
    msg=json.loads(s.recv(65535))
    print(msg['type'],msg['name'],":",msg['text'],"(",msg['id'],")")
