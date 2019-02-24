import socket
address = "127.0.0.1"
port =12000
socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((address.port))
socket.send(bytes("Hello World\n"))
socket.bind((address,port))
