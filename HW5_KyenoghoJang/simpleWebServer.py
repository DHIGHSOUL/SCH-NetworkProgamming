from socket import *
import os

HTTP_RESPONSE_200_OK = "HTTP/1.1 200 OK\r\nContent-Type: {}\r\n\r\n"
HTTP_RESPONSE_404_NOT_FOUND_HEAD = "HTTP/1.1 404 Not Found\r\n\r\n"
HTTP_RESPONSE_404_NOT_FOUND_BODY = "<HTML><HEAD>\n<TITLE>Not Found</TITLE></HEAD><BODY>Not Found</BODY></HTML>"

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 80))
sock.listen(5)

while True:
    connection, address = sock.accept()

    requestFromClient = connection.recv(1024).decode()
    requestFromClient = requestFromClient.split('\r\n')
    requestFromClient = requestFromClient[0].split(' ')
    requestFromClient = requestFromClient[1].replace('/', '')
    print(requestFromClient)

    if requestFromClient == 'index.html':
        getPath = open('index.html', 'r', encoding='utf-8')
        getFile = getPath.read()
        getPath.close()
        mimeType = 'text/html'
        header = HTTP_RESPONSE_200_OK.format(mimeType)
        connection.send(header.encode())
        connection.send(getFile.encode('euc-kr'))
        connection.close()
    else:
        errorHeader = HTTP_RESPONSE_404_NOT_FOUND_HEAD
        errorBody = HTTP_RESPONSE_404_NOT_FOUND_BODY
        connection.send(errorHeader.encode())
        connection.send(errorBody.encode())
        connection.close()
        break