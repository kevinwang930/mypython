import socket


def start_server(host='localhost', port=12345):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket to a address.
    server_socket.bind((host, port))

    # Enable server to accept connections.
    server_socket.listen(1)
    print(f'Starting socket server at {host}:{port}')

    while True:
        # Establish connection with client.
        client_socket, addr = server_socket.accept()
        print(f"Got connection from {addr}")

        # send a thank you message to the client.
        for i in range(10):
            message = f"Data {i}\n"
            client_socket.send(message.encode())

        # Close the connection with the client
        client_socket.close()


if __name__ == '__main__':
    start_server()