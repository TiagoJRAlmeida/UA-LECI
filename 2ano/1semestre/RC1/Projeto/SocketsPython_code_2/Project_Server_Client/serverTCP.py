import socket
import threading
import signal
import sys

def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

clients = {}  

def broadcast_message(sender_socket, address, message):
    message = f"\n{address[0]}:{address[1]} says: {message.decode()}".encode()
    for client_address in clients.keys():
        client_socket = clients[client_address]
        if client_socket != sender_socket:
            try:
                client_socket.send(message)
            except socket.error:
                print(f"Error broadcasting message to {client_address}")
                remove_client(client_socket)

def remove_client(client_socket):
    for client_address in clients.keys():
        if clients[client_address] == client_socket:
            del clients[client_address]
            break

def handle_client_connection(client_socket,address): 
    print('Accepted connection from {}:{}'.format(address[0], address[1]))
    try:
        while True:
            request = client_socket.recv(1024)
            if not request:
                client_socket.close()
            else:
                msg=request.decode()
                print('Received {}'.format(msg))
                broadcast_message(client_socket, address, msg.encode())
    except (socket.timeout, socket.error):
        print('Client {} error. Done!'.format(address))
        print(clients)

ip_addr = "0.0.0.0"
tcp_port = 5005

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_addr, tcp_port))
server.listen(5)  # max backlog of connections

print('Listening on {}:{}'.format(ip_addr, tcp_port))

while True:
    client_sock, address = server.accept()
    clients[address] = client_sock
    client_handler = threading.Thread(target=handle_client_connection,args=(client_sock,address),daemon=True)
    client_handler.start()


