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
        print msg
        self.socket.sendto(msg,self.destination)


# multicast 224.1.20.40 port 6020
class KController:
    def __init__(self, khost="localhost"):
        self.khost = khost
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('',4002))
        self.socket.settimeout(1.0)
        
        #self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.socket.connect((self.khost,14002))
        #self.socket.send('$KSSIS,13,EM2040P_40\r\n')
        #self.socket.send('$KSSIS,451,EM2040P_40\r\n')

        #self.socket.send('$KSSIS,458,EM2040P_40\r\n')
        
    def run(self):
        while True:
            try:
                data = self.socket.recv(4096)
                print data
            except socket.timeout:
                print 'waiting...'
                #self.socket.sendto('$KSSIS,13,EM2040P_40\r\n',(self.khost,14002))
                

if __name__ == '__main__':
    k = KController()
    k.run()
