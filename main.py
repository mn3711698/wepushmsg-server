#!/usr/bin/python
# coding:utf-8

import wxpy

def getQRCode(uuid,status,qrcode):
    print qrcode
    return

def login_success():
    return

def logout():
    return

bot=wxpy.Bot(True,False,"./QR.png",getQRCode,login_success,logout)