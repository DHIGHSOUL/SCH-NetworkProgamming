from socket import *
import random

port = 6000
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
        heartRate = str(random.randint(40, 141))
        walkingCount = str(random.randint(2000, 6001))
        burnedCalorie = str(random.randint(1000, 4001))
        sendMessage = heartRate + '/' + walkingCount + '/' + burnedCalorie
        connection.send(sendMessage.encode())
    else:
        connection.send("Invalid Command".encode())