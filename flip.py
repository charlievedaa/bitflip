#!/usr/bin/env python

import sys
import socket
import struct

if len(sys.argv) < 2:
    sys.exit('Usage: %s [hostname or IP]' % sys.argv[0])

def toggle(int_type, offset):
    mask = 1 << offset
    return(int_type ^ mask)

try:
    ip = socket.gethostbyname(sys.argv[1])
except:
    sys.exit('Usage: %s [hostname or IP]' % sys.argv[0])

ip_as_integer = struct.unpack('!I', socket.inet_aton(ip))[0]

print "{0:032b}".format(ip_as_integer) + " -> " + ip.ljust(15) + " -> " + socket.getfqdn(ip)

for i in range(0, 32):
    flipped_binary = toggle(ip_as_integer, i)
    flipped_struct = struct.pack('!I', flipped_binary)
    flipped_ip = socket.inet_ntoa(flipped_struct)
    flipped_host = socket.getfqdn(flipped_ip)
    print "{0:032b}".format(flipped_binary) + " -> " + flipped_ip.ljust(15) + " -> " + flipped_host
