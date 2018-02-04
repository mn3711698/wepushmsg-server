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
        print("Got message from user")
        sendData={'name':msg.sender.nick_name,'text':msg.text,'id':msg.id}
        print(sendData)
        self.send(json.dumps(sendData),False)
        return
    
    def send(self,msg,isQRCode):
        """
        3B      4B      0~MAX B
        TYPE    SIZE    MESSAGE
        """
        if(isQRCode):
            self.client.sendall(bytes("qrc",encoding = "utf8"))
            self.client.sendall(struct.pack('<I',len(msg)))
            self.client.sendall(msg)
        else:
            self.client.sendall(bytes("msg",encoding = "utf8"))
            msg_bytes=bytes(msg,encoding = "utf8")
            self.client.sendall(struct.pack('<I',len(msg_bytes)))
            self.client.sendall(msg_bytes)
        return

    def getQRCode(self,uuid,status,qrcode):
        if(self.noSended):
            print("UUID:",uuid)
            print("Sending QR code.")
            self.send(qrcode,True)
            self.noSended=False
        print("Status:",status)
        return

    def loginSuccess(self):
        print("Your account logged in successfully.")
        return

    def logout(self):
        print("Your account was logged out.")
        return

    def __init__(self,c):
        self.client=c
        self.bot=wxpy.Bot(True,2,None,self.getQRCode,self.loginSuccess,self.logout)
        self.bot.register(chats=wxpy.User,msg_types='Text')(self.receiveMsgUser)
        while(True):pass
