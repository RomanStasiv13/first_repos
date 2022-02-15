import socket
from caesar_encrypt import encrypt

HOST = '127.0.0.1'
PORT = 6666


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

while True:
    conn, addr = server.accept()
    try:
        print(f'connected to {addr}')
        all_data = []
        while len(all_data) != 2:
            data = conn.recv(1024).decode()
            if data:
                all_data.append(data)
        print(all_data)
        conn.send(encrypt(all_data[0],int(all_data[1])).encode())
    finally:
        conn.close()
