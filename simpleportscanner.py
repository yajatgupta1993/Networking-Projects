#!/usr/bin/python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("[*] Enter the host to scan: ")
port = int(input("[*] Enter the host to scan: "))

def portscanner(port):
    if sock.connect_ex((host,port)):
        print ("Port %d is closed" % (port))
    else:
        print ("Port %d is open" % (port))

portscanner(port)
