import socket

HOST = '127.0.0.1'
PORT = 6666



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    client_text = input('Please enter the text you want to ecrypt: ')
    s.sendall(client_text.encode())
    shift_step = input('Enter which shift step you want: ')
    s.sendall(shift_step.encode())
    data = s.recv(1024)

print("Received", repr(data.decode()))