#!/usr/bin/python
# SERVER SIDE
import socket

# Soket nesnesi
s = socket.socket()
host = socket.gethostname()
port = 55555
s.bind((host, port))

s.listen(5)

while True:
        c, addr = s.accept()
        print('BAGLANTI ', addr)
        c.send('MERHABA KULLANICI')
        c.close()
