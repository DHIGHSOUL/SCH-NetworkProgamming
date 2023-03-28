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

    # 문자열 파싱
    parsingOpeartion = calculateOperation.split()
    firstOperand = int(parsingOpeartion[0])
    operator = parsingOpeartion[1]
    secondOperand = int(parsingOpeartion[2])

    if operator == '+':
        print(firstOperand + secondOperand)
    elif operator == '-':
        print(firstOperand - secondOperand)
    elif operator == '*':
        print(firstOperand * secondOperand)
    elif operator == '/':
        divideOperands = firstOperand/secondOperand
        print('%.1f' % divideOperands)