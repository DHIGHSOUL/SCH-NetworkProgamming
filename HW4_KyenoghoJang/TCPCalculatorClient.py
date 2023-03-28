import socket

port = 5959
BUFSIZE = 1024

address = ('localhost', port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True:
    operation = input("Operation to send: ")
    s.send(operation.encode())

s.close()