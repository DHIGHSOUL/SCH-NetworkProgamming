import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 6000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

# 서버로 이름 전달
name = "Kyenogho Jang"
sock.send(name.encode())

# 서버에서 학번 전달받아 출력
studentNumber = sock.recv(8)
numberCheck = int.from_bytes(studentNumber, 'big')
print(numberCheck)

sock.close()