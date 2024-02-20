import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))          
s.listen(5)
 
while True:
    clt,adr=s.accept()
    print(f"Connection to {adr}established")  
   #f string is literal string prefixed with f which 
   #contains python expressions inside braces
    clt.send(bytes("Socket Programming in Python","utf-8")) #to send inpy