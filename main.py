#!/usr/bin/python3
#coding:utf-8

import wxpy
import socket
import json

class Pusher:
    client=None
    bot=None
    noSended=True

    with open('config.json','r') as file:
        jsondata=json.load(file)

    def receiveMsg(self,msg):
        print("Getted messege")
        sendData={'type':msg.type,'name':msg.sender.nick_name,'text':msg.sender.text,'id':msg.id}
        self.client.send(json.dumps(sendData))
        return
    
    def getQRCode(self,uuid,status,qrcode):
        if(self.noSended):
            print("Sending QR code.")
            self.client.send(qrcode)
            self.noSended=False
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
        func=self.bot.register()
        func(self.receiveMsg)
