from socket import *

HOST = ''
PORT = 5007

s = socket(AF_INET, SOCK_STREAM)

s.bind((HOST, PORT))

print(f"socket: {s}")

s.listen(5)

# the code example in the lecture was throwing an OSerror 22: Invalid argument
# based in this link: https://docs.python.org/3/howto/sockets.html
# im trying to resolve this telling the server to queue requests before connecting
(conn, addr) = s.accept()


while True:
    data = conn.recv(1024)
    
    if not data: break
    
    msg = data.decode()+'\nHello Client!'
    
    conn.send(msg.encode())
    conn.close()
    