#!/usr/bin/python3
#coding:utf-8

import wxpy
import socket

class Pusher:
    client=None
    bot=None
    
    def getQRCode(self,uuid,status,qrcode):
        print("UUID:",uuid)
        print("Status:",status)
        self.client.send(qrcode)
        return

    def login_success(self):
        return

    def logout(self):
        return

    def __init__(self,c):
        self.client=c
        self.bot=wxpy.Bot(True,2,None,self.getQRCode,self.login_success,self.logout)
