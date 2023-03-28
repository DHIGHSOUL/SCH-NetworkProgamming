import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 6000))
s.listen(10)

while True:
    client, addr = s.accept()
    print('Connection from', addr)
    client.send(b'Hello ' + addr[0].encode())

    # 클라이언트에게 이름 받아서 출력
    clientName = client.recv(1024)
    print(clientName.decode())

    # 클라이언트에게 학번을 전달(문자열이 아닌 정수로 전달)
    studentNumber = 20181520
    sendNumber = studentNumber.to_bytes(8, 'big')
    client.send(sendNumber)

    client.close()