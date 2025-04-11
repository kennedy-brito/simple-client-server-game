from socket import *

HOST = ''
PORT = 5007

s = socket(AF_INET, SOCK_STREAM)

s.bind((HOST, PORT))

print(f"socket: {s}")

s.listen(5)

# the code example in the lecture was throwing an OSerror 22: Invalid argument
# when `s.accept()` was called
# based in this link: https://docs.python.org/3/howto/sockets.html
# im trying to resolve this telling the server to queue requests before connecting

# TODO: It doesn't end successfuly when using CTRL-C, it kills the access but the port continues in use

while True:
    (conn, addr) = s.accept()
    data = conn.recv(1024)
    
    if not data: break
    
    print(data.decode())
    msg = data.decode()+'\nHello Client!'
    
    conn.send(msg.encode())
    conn.close()
    