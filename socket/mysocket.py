# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#An example script to connect to Google using socket 
# programming in Python 
import socket # for socket 
import sys,time
  
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print ("Socket successfully created")
except socket.error as err: 
    print ("socket creation failed with error %s" %(err)) 
  
# default port for socket 
port = 5000
  
host_ip = '192.168.1.66' 
# connecting to the server 
s.connect((host_ip, port)) 
  
print ("the socket has successfully connected to bing"
       " on port == %s" %(host_ip) ) #
time.sleep(5)

s.close()