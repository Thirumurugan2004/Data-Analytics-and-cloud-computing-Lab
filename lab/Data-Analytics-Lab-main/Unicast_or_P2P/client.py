#Python p2p Client
import socket

# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))

while True:
    try:
        # Send message to server
        message = input("Enter your message: ")
        client.send(message.encode('utf-8'))

        # Receive response from server
        response = client.recv(1024).decode('utf-8')
        print("Server says:", response)
    except Exception as e:
        print("Error:", e)
        break

# Close connection
client.close()

