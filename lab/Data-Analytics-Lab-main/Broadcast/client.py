#PYTHON BROADCAST CLIENT

import socket

# Set up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Set up server address and port
server_address = ('', 12345)  # Empty string for server address means it will bind to all available interfaces
server_socket.bind(server_address)


while True:
    message, client_address = server_socket.recvfrom(1024)
    print(f"Received message from {client_address}: {message.decode()}")

