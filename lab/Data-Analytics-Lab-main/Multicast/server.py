#PYTHON MULTICAST SERVER

import socket
import threading

def multicast_messages(server_socket, client_ips):
    multicast_group = "224.0.0.1"
    port = 8081

    multicast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    multicast_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

    while True:
        message = input("Enter message to multicast: ")
        if(message.lower=='quit'):
        	break
        for client_ip in client_ips:
            multicast_socket.sendto(message.encode(), (client_ip, port))


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8080))
server_socket.listen(5)

client_ips = ["127.0.0.1", "10.11.147.7", "10.11.157.229"]
#APPEND THE IP OF SYSTEM FOR WHICH U WANT TO SEND MESSAGE

multicast_thread = threading.Thread(target=multicast_messages, args=(server_socket, client_ips))

multicast_thread.start()

multicast_thread.join()
