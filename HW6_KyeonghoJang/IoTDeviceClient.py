import socket
import time

device1Port = 5959
device2Port = 6000
BUFSIZE = 1024

address1 = ('localhost', device1Port)
address2 = ('localhost', device2Port)

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect(address1)
s2.connect(address2)

while True:
    clientCommand = input("Command to send: ")
    if clientCommand == 'quit':
        s1.close()
        s2.close()
        break
    elif clientCommand == '1':
        command = 'Request'
        s1.send(command.encode())
        result = s1.recv(BUFSIZE).decode()
        device1Result = result.split('/')
        nowDate = time.strftime('%c', time.localtime(time.time()))
        saveResultString = nowDate + ': ' + 'Device1: Temp=' + device1Result[0] + ', Humid=' + device1Result[1] + ', Iilum=' + device1Result[2] + '\n'
        filePath = open('device1Result.txt', 'a')
        filePath.write(saveResultString)
        filePath.close()
    elif clientCommand == '2':
        command = 'Request'
        s2.send(command.encode())
        result = s2.recv(BUFSIZE).decode()
        device2Result = result.split('/')
        nowDate = time.strftime('%c', time.localtime(time.time()))
        saveResultString = nowDate + ': ' + 'Device2: Heartbeat=' + device2Result[0] + ', Steps=' + device2Result[1] + ', Cal=' + device2Result[2] + '\n'
        filePath = open('device2Result.txt', 'a')
        filePath.write(saveResultString)
        filePath.close()