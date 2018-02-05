#!/usr/bin/python3
#coding:utf-8

import wxpy
import socket
import json
import struct

class Pusher:
    client=None
    bot=None
    noSended=True

    with open('config.json','r') as file:
        jsondata=json.load(file)

    def receiveMsgUser(self,msg):
        print("Got message from a user.(ID:",msg.id,")")
        sendData={\
        'sdtp':'user',\
        'name':msg.sender.nick_name,\
        'type':msg.type,\
        'cont':msg.text,\
        'id':msg.id\
        }
        self.send(json.dumps(sendData))
        return

    def receiveMsgGroup(self,msg):
        print("Got message from a group.(ID:",msg.id,")")
        sendData={\
        'sdtp':'group',\
        'group':msg.sender.nick_name,\
        'name':msg.member.name,\
        'type':msg.type,\
        'cont':msg.text,\
        'id':msg.id\
        }
        self.send(json.dumps(sendData))
    
    def send(self,content,isBytes=False,tp='msg'):
        """
        3B      4B      0~MAX B
        TYPE    SIZE    CONTENT
        """
        if(len(tp)!=3):
            raise TypeError
        if(isBytes):
            self.client.sendall(bytes(tp,encoding='utf8'))
            self.client.sendall(struct.pack('<I',len(content)))
            self.client.sendall(content)
        else:
            self.client.sendall(bytes(tp,encoding="utf8"))
            content_bytes=bytes(content,encoding="utf8")
            self.client.sendall(struct.pack('<I',len(content_bytes)))
            self.client.sendall(content_bytes)
        return

    def getQRCode(self,uuid,status,qrcode):
        if(self.noSended):
            print("UUID:",uuid)
            print("Sending QR code.")
            self.send(qrcode,True,'qrc')
            self.noSended=False
        print("Status:",status)
        return

    def loginSuccess(self):
        print("Your account logged in successfully.")
        self.send("Successfull",tp='suc')
        return

    def logout(self):
        print("Your account was logged out.")
        return

    def __init__(self,c):
        self.client=c
        self.bot=wxpy.Bot(True,2,None,self.getQRCode,self.loginSuccess,self.logout)
        self.bot.register(chats=wxpy.User)(self.receiveMsgUser)
        self.bot.register(chats=wxpy.Group)(self.receiveMsgGroup)
        while(True):pass
