import socket

SEND = "TRACE / HTTP/1.1\r\nHost: Localhost:1300"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",1300))

s.send(SEND.encode())
data=s.recv(1024)
data2 = s.recv(1024)
print(data.decode(),data2.decode())

s.close()