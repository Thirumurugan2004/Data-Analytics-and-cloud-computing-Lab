import socket
import threading

host = 'localhost'
port = 12347
    

def send_message(client_socket):
    while True:
        try:
            message = input("Enter message: ")
            client_socket.sendall(message.encode())
        except:
            break

def receive_message(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            print(f"Server: {data.decode()}")
        except:
            break

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
    send_thread.start()
    receive_thread.start()
    send_thread.join()
    receive_thread.join()


    
start_client(host, port)


