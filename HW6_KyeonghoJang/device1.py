from socket import *
import random

port = 5959
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

connection, (remotehost, remoteport) = sock.accept()
print('connected by', remotehost, remoteport)

while True:
    # 명령 수신
    clientCommand = connection.recv(BUFSIZE).decode()
    if clientCommand == 'quit':
        connection.close()
        break
    elif clientCommand == 'Request':
        temparature = str(random.randint(0, 41))
        humidity = str(random.randint(0, 101))
        illumination = str(random.randint(70, 151))
        sendMessage = temparature + '/' + humidity + '/' + illumination
        connection.send(sendMessage.encode())
    else:
        connection.send("Invalid Command".encode())