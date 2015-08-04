#Echo client program
import socket


HOST = '10.32.105.213'
PORT = 6667
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(HOST,PORT)
s.sendall('hello,world')
s.close()
print 'Recived', repr(data)
