#!/usr/bin/python3

import socket
import sys

BROADCAST4 = "255.255.255.255"
UDP_PORT = 4992

uctargets = [
        "172.30.251.99",
        "172.30.250.126",
        "10.100.0.4",
        "10.100.0.6",
        "10.100.0.8",
        "10.100.0.10",
        "10.100.0.12" ]


recvsock = socket.socket(socket.AF_INET, 
                         socket.SOCK_DGRAM)
recvsock.bind((BROADCAST4, UDP_PORT))

sendsock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM) 

while True:
    data, addr = recvsock.recvfrom(1500) # hello ethernet
#    print("received message from: %s\n", addr)

    sys.stdout.write("R")
#    sys.stdout.flush()
    for tgtaddr in uctargets:
      sendsock.sendto(data, (tgtaddr, UDP_PORT))
      sys.stdout.write("T")
      sys.stdout.flush()


