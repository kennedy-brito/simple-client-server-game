from socket import *
from game import Game

HOST = ''
PORT = 5007

s = socket(AF_INET, SOCK_STREAM)

s.bind((HOST, PORT))

print(f"socket: {s}")

# the code example in the lecture was throwing an OSerror 22: Invalid argument
# when `s.accept()` was called
# based in this link: https://docs.python.org/3/howto/sockets.html
# im trying to resolve this telling the server to queue requests before connecting: this way it was resolved
s.listen()

game = Game()
while True:
    print("Waiting for client command")
    (conn, addr) = s.accept()
    data = conn.recv(1024)
    
    if not data: 
        conn.close()
        break
    command = data.decode()
    
    print(command + " was the client command!")
    
    game.move(command)
    
    map = game.print_map()
    
    conn.send(map.encode())