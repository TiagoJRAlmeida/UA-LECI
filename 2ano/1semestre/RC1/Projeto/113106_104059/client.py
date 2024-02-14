import socket
import threading
import signal
import sys

def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

ip_addr = "201.139.6.194"
tcp_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((ip_addr, tcp_port))

def receive_messages():
    while True:
        try:
            response = sock.recv(4096).decode()
            print(response)
            print('Message to send?', end='', flush=True)
        except (socket.timeout, socket.error):
            print('Server error. Done!')
            sys.exit(0)

receive_thread = threading.Thread(target=receive_messages, daemon=True)
receive_thread.start()
hostname = socket.gethostname()
print('Message to send?', end='', flush=True)

while True:
    try:
        message = input().encode()
        if len(message) > 0:
            hostname = socket.gethostname()
            data_to_send = f"{hostname}: {message.decode()}"
            sock.send(data_to_send.encode())
    except (socket.timeout, socket.error):
        print('Server error. Done!')
        sys.exit(0)
