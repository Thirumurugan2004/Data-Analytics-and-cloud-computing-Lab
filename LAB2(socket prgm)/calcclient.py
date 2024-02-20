import socket

SERVER = socket.gethostname()
PORT = 1357
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((SERVER, PORT))
print("Example : (4 + 5) or (4 - 5) or (4 * 5) or (4 / 5)")
while True:
	inp = input("Enter the operation in the form opreand operator oprenad: ")
	if inp == "Over":
		break
	client.send(inp.encode())

	answer = client.recv(1024)
	print("Answer is "+answer.decode(),"\n")
	print("Type 'Over' to terminate")

client.close()
