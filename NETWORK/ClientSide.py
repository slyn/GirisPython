#!/usr/bin/python
#CLIENT SIDE
import socket

#Soket nesnesi
s = socket.socket()
host = socket.gethostname()
port = 55555

s.connect((host,port))
print(s.recv(1024))
s.close()