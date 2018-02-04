#!/usr/bin/python3
#coding:utf-8

import socket
import json
import struct

s=socket.socket()
s.connect(("127.0.0.1",8888))
print("Connected!")
while(True):
    """
    {
        "name":USERNAME,
        "text":TEXT,
        "id":ID
    }
    """
    str_type=str(s.recv(3),encoding = "utf8")
    print("Got a message.")
    size=s.recv(4)
    str_size=struct.unpack('<I',size)[0]
    if(str_type=='qrc'):
        print("It is a qrcode.")
        f=open('qr.png','wb+')
        f.write(s.recv(str_size))
        f.close()
    elif(str_type=='msg'):
        print("It is a message.")
        msg=json.loads(str(s.recv(str_size),encoding = "utf8"))
        print(msg['name'],":",msg['text'],"(",msg['id'],")")
