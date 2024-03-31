import socket
import ssl

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile='cert/ca.pem')
context.load_cert_chain(certfile="cert/client/cert.pem", keyfile="cert/client/key.pem", password="hello")

conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname='localhost')
conn.connect(('localhost', 8443))

print("SSL established. Peer: {}".format(conn.getpeercert()))
print("Sending: 'Hello, server!'")
conn.send(b"Hello, server!")
buf = conn.recv(1024)
print("Received from server: {}".format(buf))

print("Closing connection")
conn.close()