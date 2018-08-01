#!/usr/bin/env python

import socket

# udp port 4001: R20
# udp port 4002: R00, R10, R12
#
class EM:
    def __init__(self, sis_ip, model_number='2040'):
        self.model_number = model_number
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.destination = (sis_ip,4002)

    def stopPinging(self):
        #talker id, picking BS for backseat for now...
        msg = '$BSR00,EMX='+self.model_number+',ROP=,SID=,PLN=,PLL=,COM=\r\n'
        self.socket.sendto(msg,self.destination)

    def startPinging(self):
        msg = '$BSR10,EMX='+self.model_number+',ROP=,SID=,PLN=,PLL=,COM=\r\n'
        self.socket.sendto(msg,self.destination)

    def startLine(self,line):
        if line < 0:
            msg = '$BSR12,EMX='+self.model_number+',ROP=,SID=,PLN=,PLL=,COM=\r\n'
        else:
            msg = '$BSR12,EMX='+self.model_number+',ROP=,SID=,PLN=,PLL='+str(line)+',COM=\r\n'
        self.socket.sendto(msg,self.destination)

if __name__ == '__main__':
    em = EM('stormi')
    em.startLine('11')
