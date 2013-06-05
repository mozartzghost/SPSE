#!/usr/bin/python
#
# Network sniffer for Linux
# Mark Osborn 05/06/2013
#
# To Do:
# Improve the granularity of unpacking to get IP version number correctly
# Set promiscuous mode automatically
# Allow choice of interface to attach to
#

import socket
import struct
import binascii

while True:

        rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

        pkt = rawSocket.recvfrom(2048)
        #split out the headers
        ethernetHeader = pkt[0][0:14]
        ipHeader = pkt[0][14:34]
        tcpHeader = pkt[0][34:54]
        raw_data = pkt[0][55:]
        data = binascii.hexlify(raw_data)
        #unpack the ethernet header into component parts
        eth_hdr = struct.unpack("!6s6s2s", ethernetHeader)
        #parse ethernet header
        src_eth = binascii.hexlify(eth_hdr[0])
        dst_eth = binascii.hexlify(eth_hdr[1])

        #unpack the IP header into component parts
        ip_hdr = struct.unpack("!1s1s2s4s1s1s2s4s4s", ipHeader)
        #parse IP header
        version = binascii.hexlify(ip_hdr[0])
        typ_serv = binascii.hexlify(ip_hdr[1])
        protocol = binascii.hexlify(ip_hdr[5])
        hdr_chksum = binascii.hexlify(ip_hdr[6])
        src_ip = socket.inet_ntoa(ip_hdr[7])
        dst_ip = socket.inet_ntoa(ip_hdr[8])
        length = binascii.hexlify(ip_hdr[2])
        ttl = binascii.hexlify(ip_hdr[4])

        #unpack TCP header
        tcp_hdr = struct.unpack("!2s2s4s4s8s", tcpHeader)
        #parse TCP header
        src_port = binascii.hexlify(tcp_hdr[0])
        dst_port = binascii.hexlify(tcp_hdr[1])
        seq_num = binascii.hexlify(tcp_hdr[2])
        ack_num = binascii.hexlify(tcp_hdr[3])

        #Output info to user
        print "[+] ETHERNET"
        print "[+] Src MAC address: " + src_eth
        print "[+] Dst MAC address: " + dst_eth
        print "[+] IP"
        print "[+]      Src IP address: " + src_ip
        print "[+]      Dst IP address: " + dst_ip
        print "[+]      IP version: " + version
        print "[+]      Protocol: " + protocol
        print "[+]      Type of Service: " + typ_serv
        print "[+]      Total Length: " + length
        print "[+]      Checksum: " + hdr_chksum
        print "[+]      TTL: " + ttl
        print "[+] TCP"
        print "[+]              TCP Src Port: " + src_port
        print "[+]              TCP Dst Port: " + dst_port
        print "[+]              TCP Seq Num: " + seq_num
        print "[+]              TCP Ack Num: " + ack_num
        print "[+] DATA\n" + data
        print "========================================================"


