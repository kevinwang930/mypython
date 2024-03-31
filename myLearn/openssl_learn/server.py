from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl



if __name__ == '__main__':

    httpd = HTTPServer(('localhost', 12345), BaseHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket, keyfile="cert/server/client_key.pem", certfile='cert/server/cert.pem', server_side=True)
    httpd.serve_forever()