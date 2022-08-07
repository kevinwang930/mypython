# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 15:55:05 2020

@author: kevin
"""



# first of all import the socket library 
import socket                
import selectors 
import types
# next create a socket object 
s = socket.socket()     

#reuse socket port in time wait mood
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   
print ("Socket successfully created")
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345                
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)      
print ("socket is listening")            
s.setblocking(False)
sel = selectors.DefaultSelector()
sel.register(s, selectors.EVENT_READ, data=None)
# a forever loop until we interrupt it or  



def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)
    ndata = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    #conn.send(b'hello')
    sel.register(conn, events, data=ndata)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print('closing connection to', data.addr)
            sel.unregister(sock)   
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('echoing', repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb)  # Should be ready to write
            print('message send successfully')
            data.outb = data.outb[sent:]


while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data is None:
            accept_wrapper(key.fileobj)
        else:
            service_connection(key, mask)
   
