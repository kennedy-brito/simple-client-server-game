from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.connect((HOST, PORT))

msg = "Hello Server!"

s.send(msg.encode())

data = s.recv(1024)

print(data.decode())
s.close()