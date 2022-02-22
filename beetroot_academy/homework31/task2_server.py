# Task 2
# Echo server with threading
# Create a socket echo server which handles each connection in a separate Thread


import socket
import threading

HOST = '127.0.0.1'
PORT = 6161
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
thread_counter = 0

def client_thread(connection):
    while True:
        data = connection.recv(1024)
        reply = f'[RECEIVED FROM CLIENT]:{data.decode("utf-8")}'
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()


print('[STARTING]...')
server_socket.bind((HOST, PORT))
server_socket.listen(6)
print(f'[LISTENING] server on {HOST}:{PORT}')

while True:
    connection,address = server_socket.accept()
    thread = threading.Thread(target=client_thread, args=(connection,))
    thread.start()
    thread_counter+=1
    print(f'Threads: {thread_counter}')


