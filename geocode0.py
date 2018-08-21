#for linux
#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import socket
from urllib.parse import quote_plus
request="""\
GET /maps/api/geocode/json?address={}&sensor=false HTTP/1.1\r\n
Host: maps.google.com:80\r\n
User-agent: geocode0.py\r\n
Connection: close\r\n
\r\n
"""
def geocode(address):
	sock = socket.socket()
	sock.connect(('maps.google.com',80))
	requests = request.format(quote_plus(address))
	sock.sendall(requests.encode('ascii'))
	reply = b''
	while True:
		data = sock.recv(4096)
		if not data:
			break
		reply += data
		print(reply.decode('utf-8'))
if __name__ == '__main__':
	geocode("x")#x ur address
