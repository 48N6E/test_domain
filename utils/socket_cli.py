import socket

HOST= 'baidu.com'
port = 80
BUFFER= 4096

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((HOST,port))
sock.send(b'hello')
recv = sock.recv(BUFFER)
print('[tcpServer said]: %s '% recv)
sock.close()