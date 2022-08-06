#!/bin/python

import socket
import sys

if len(sys.argv) != 3:
        print("Usage: python smtpVRFY.py <username> <ip>")
        sys.exit(0)

username = sys.argv[1]
ip = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connect = s.connect((ip,25))

banner = s.recv(1024)
print(banner.decode('utf-8'))

message = bytes('VRFY ' + username + '\r\n', 'utf-8')
s.send(message)
result = (s.recv(1024))

print(result.decode('utf-8'))

s.close()
