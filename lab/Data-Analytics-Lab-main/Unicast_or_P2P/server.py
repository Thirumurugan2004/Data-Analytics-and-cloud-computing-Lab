#Python p2p Server

import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print("Client says:", message)

            # Send message to client
            response = input("Enter your message: ")
            client_socket.send(response.encode('utf-8'))
        except Exception as e:
            print("Error:", e)
            break

    # Close connection
    client_socket.close()


# Set up server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8888))
server.listen(5)
print("Server listening on port 8888...")

while True:
    # Accept client connection
    client_socket, addr = server.accept()
    print("Accepted connection from", addr)

    # Create a thread to handle client
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
