# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 22:04:33 2020

@author: kevin
"""


import socket			 
import selectors 
import time
# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 12345				
host = '127.0.0.1'
server_addr = (host,port)



sel = selectors.DefaultSelector()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.setblocking(False)
sock.connect(server_addr)
time.sleep(1)
events = selectors.EVENT_READ | selectors.EVENT_WRITE

data = (b'hello')
sel.register(sock, events, data=data)
        
event = sel.select(timeout=None)
print(event[0][1])


sock.shutdown(2)
sock.close()