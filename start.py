#!/usr/bin/python
#coding:utf-8

import json
import socket
import main

with open('config.json','r') as file:
    jsondata=json.load(file)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=jsondata['host']
port=jsondata['port']
s.bind((host,port))
print "Host:",host
print "Port:",port

s.listen(jsondata['listen_max'])
print "Socket is listening."
while True:
    c,addr=s.accept()
    print "Connected!"
    print "Client IP:",addr
    main.Pusher(c)
