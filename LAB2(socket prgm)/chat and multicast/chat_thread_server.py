import socket
import threading

host = 'localhost'
port = 12347

def handle_client(client_socket, address):
    while True:
        try:
            # Receive data from client
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received message from {address}: {data.decode()}")

            # Echo the message back to the client
            client_socket.sendall(data)
        except:
            break

    # Close client socket
    client_socket.close()
    print(f"Connection with {address} closed.")

def receive_messages(server_socket):
    while True:
        client_socket, address = server_socket.accept()
        print(f"Accepted connection from {address}")

        # Add client socket to the list of connected clients
        connected_clients.append(client_socket)

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

def send_messages(server_socket):
    while True:
        message = input("Enter message to send: ")
        message = message.encode()
        for client_socket in connected_clients:
            try:
                client_socket.sendall(message)
            except:
                # If sending fails, remove the client socket
                client_socket.close()
                connected_clients.remove(client_socket)

# List to store connected client sockets
connected_clients = []

def start_server(host, port):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    # Start threads for receiving and sending messages
    receive_thread = threading.Thread(target=receive_messages, args=(server_socket,))
    send_thread = threading.Thread(target=send_messages, args=(server_socket,))
    receive_thread.start()
    send_thread.start()

    # Join threads
    receive_thread.join()
    send_thread.join()


   
start_server(host, port)


