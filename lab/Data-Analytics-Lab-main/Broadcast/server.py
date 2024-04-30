#PYTHON BROADCAST SERVER

import socket

# Set up client socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

client_address = ('<broadcast>', 12345)  # Broadcasting to all available interfaces

while True:
    message = input("Enter message to broadcast: ")
    if(message.lower()=='quit'):
    	break
    server_socket.sendto(message.encode(), client_address)
 
