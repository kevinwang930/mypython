# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:18:47 2020

@author: kevin
"""


# Import socket module 
import socket			 
import selectors 
import types
# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 12345				
host = '192.168.1.66'


messages = ['Hello from client.','Hello from client.',
            'Hello from client.']
sel = selectors.DefaultSelector()

def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print('starting client', connid, 'to', server_addr)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        #events = selectors.EVENT_READ | selectors.EVENT_WRITE
        events = selectors.EVENT_WRITE
        data = types.SimpleNamespace(addr=server_addr,
                                     connid = connid,
                                     messages=list(messages),
                                     outb=b'')
        sel.register(sock, events, data=data)
        
def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            print('received', repr(recv_data), 'from server')
            sel.unregister(sock)
            events = selectors.EVENT_WRITE
            sel.register(sock,events,data)
        if not recv_data:
            print('closing connection client', data.connid)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if not data.outb and data.messages:
            data.outb = (data.messages.pop(0) + str(data.connid)).encode('utf-8')
        if data.outb:
            print('client {} sending data'.format(data.connid))
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]
            sel.unregister(sock)
            events = selectors.EVENT_READ
            sel.register(sock,events,data)
        else:
            print('all message send out')
            sel.unregister(sock)
            sock.close()

start_connections(host,port,2)
while True:
    if sel._readers or sel._writers:
        events = sel.select(timeout=None)

        for key, mask in events:
            service_connection(key, mask)
    else:
        break
 
