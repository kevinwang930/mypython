import socket
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert/server/cert.pem", keyfile="cert/server/key.pem", password="hello")

bindsocket = socket.socket()
bindsocket.bind(('localhost', 8443))
bindsocket.listen(5)

while True:
    print("Waiting for client")
    newsocket, fromaddr = bindsocket.accept()
    print("Client connected: {}:{}".format(fromaddr[0], fromaddr[1]))
    connstream = context.wrap_socket(newsocket, server_side=True)
    try:
        print("SSL established. Peer: {}".format(connstream.getpeercert()))
        buf = connstream.recv(1024)
        print("Received from client: {}".format(buf))
        connstream.send(b"Echo: " + buf)
    finally:
        print("Closing connection")
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()