import socket
address = "127.0.0.1"
port =12000
socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind((address,port))
socket.listen(1)
conn=socket.accept()
print(conn.recv(1024))