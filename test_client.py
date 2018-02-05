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
        "sdtp":SENDER_TP,
        "group":GROUPNAME,  //Only group message.
        "name":USERNAME,
        "type":MSG_TYPE,
        "cont":MSG_CONT,
        "at":IS_AT,         //Only group message.
        "id":ID
    }
    """
    str_type=str(s.recv(3),encoding="utf8")
    size=s.recv(4)
    str_size=struct.unpack('<I',size)[0]
    if(str_type=='qrc'):
        print("Scan the qrcode to log in.")
        f=open('qr.png','wb+')
        f.write(s.recv(str_size))
        f.close()
    elif(str_type=='suc'):
        print(str(s.recv(11),encoding="utf8"))
    elif(str_type=='msg'):
        msg=json.loads(str(s.recv(str_size),encoding="utf8"))
        if(msg['sdtp']=='user'):
            print('['+msg['type']+']'+"User",msg['name'],":",msg['cont'],"("+str(msg['id'])+")")
        elif(msg['sdtp']=='group'):
            print('['+msg['type']+']'+"Group",msg['group'],\
            '@' if msg['at'] else '*'\
            ,msg['name'],":",msg['cont'],"("+msg['id']+")")
