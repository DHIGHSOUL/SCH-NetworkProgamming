from socket import *

port = 5959
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(5)

connection, (remotehost, remoteport) = sock.accept()
print('connected by', remotehost, remoteport)

while True:
    # 계산식 입력
    calculateOperation = connection.recv(BUFSIZE).decode()
    if calculateOperation == 'q':
        break
    elif not calculateOperation:
        break

    # 공백이 발견될 시 제거
    calculateOperation = calculateOperation.replace(" ", "")

    # 연산 수행
    if (calculateOperation.find('+') != -1):
        calculate = calculateOperation.split('+')
        first, second = int(calculate[0]), int(calculate[1])
        result = first + second
    elif (calculateOperation.find('-') != -1):
        calculate = calculateOperation.split('-')
        first, second = int(calculate[0]), int(calculate[1])
        result = first - second
    elif (calculateOperation.find('*') != -1):
        calculate = calculateOperation.split('*')
        first, second = int(calculate[0]), int(calculate[1])
        result = first * second
    elif (calculateOperation.find('/') != -1):
        calculate = calculateOperation.split('/')
        first, second = float(calculate[0]), float(calculate[1])
        result = first / second

    if isinstance(result, float):
        resultToString = "%.1f" % result
    else:
        resultToString = str(result)

    # 클라이언트로 전달
    connection.send(resultToString.encode())