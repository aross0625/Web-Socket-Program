# UDP_pinger_client.py

from socket import *
from datetime import datetime
from time import time

def main():
    serverName = ''
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = 'ping'
    i = 0
    count = 10
    print ('Wait: pings in progress.\n')
    while count > i:
        i = i + 1
        print ('Currently attempting ping number ', i)
        t1 = datetime.now()
        clientSocket.sendto(message.encode(),(serverName,serverPort))
        clientSocket.settimeout(1)
        try:
            modifiedMessage,serverAddress = clientSocket.recvfrom(1024)
            t2 = datetime.now()
            tt = t1 - t2
            print (modifiedMessage)
            print ('The RRT is : ',tt.microseconds, 'microseconds\n')
        except timeout:
            print ('The request has timed out')
    if i == 10:
        clientSocket.close
    pass
if __name__ == '__main__':
    main()
