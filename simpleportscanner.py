#!/usr/bin/python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.43.190"
port = 21

def portscanner(port):
    if sock.connect_ex((host,port)):
        print ("Port %d is closed" % (port))
    else:
        print ("Port %d is open" % (port))

portscanner(port)