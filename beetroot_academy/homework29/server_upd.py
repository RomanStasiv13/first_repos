import socket

HOST = '127.0.0.1'
PORT = 6666

udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_sock.bind((HOST, PORT))

while True:
    data, addr = udp_sock.recvfrom(4096)
    print(f'Client {addr} connected')
    print(f'Received dats: {data}')
    udp_sock.sendto(b'(UDP SERVER: YOUR DATA WAS RECEIVED) Hello client',addr)





