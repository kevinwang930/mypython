# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:13:49 2020

@author: kevin
"""


# telnet program example
import socket, select, string, sys,threading

def prompt() :
	sys.stdout.write('<You> ')
	sys.stdout.flush()

#main function
if __name__ == "__main__":
	
# 	if(len(sys.argv) < 3) :
# 		print ('Usage : python telnet.py hostname port')
# 		sys.exit()
	
	host = '192.168.1.66'
	port = 5000
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)
	
	# connect to remote host
	try :
		s.connect((host, port))
	except :
		print ('Unable to connect')
		sys.exit()
	
	print ('Connected to remote host. Start sending messages')
	prompt()
    
    
    
def send_msg(sock):
    while True:
        data = input()
        sock.sendall(data.encode('utf-8'))
       

def recv_msg(sock):
    connection_list =[]
    connection_list.append(sock)
    while True:
        
        read_sockets,write_sockets,error_sockets = select.select(connection_list,[],[])
        data, addr = sock.recv(1024)
        sys.stdout.write(data.decode('utf-8'))
        
	
threading.Thread(target=send_msg, args=(s,)).start()  
threading.Thread(target=recv_msg, args=(s,)).start()
                 
                 
                 