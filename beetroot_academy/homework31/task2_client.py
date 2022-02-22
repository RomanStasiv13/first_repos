# Task 2
# Echo server with threading
# Create a socket echo server which handles each connection in a separate Thread



import socket

HOST = '127.0.0.1'
PORT = 6161



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'TEST')
    data = s.recv(1024)
    print(repr(data.decode()))