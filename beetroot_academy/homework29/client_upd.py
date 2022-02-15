import socket

HOST = '127.0.0.1'
PORT = 6666

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_client:
    udp_client.sendto(b'Hello server', (HOST, PORT))
    data = udp_client.recvfrom(4096)
    print(data)
