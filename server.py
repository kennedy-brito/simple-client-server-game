from socket import *
from game import Game

def server(host, port):
    s = socket(AF_INET, SOCK_STREAM)

    s.bind((host, port))

    # the code example in the lecture was throwing an OSerror 22: Invalid argument
    # when `s.accept()` was called
    # based in this link: https://docs.python.org/3/howto/sockets.html
    # im trying to resolve this telling the server to queue requests before connecting: this way it was resolved
    s.listen()

    game = Game()
    while True:
        (conn, addr) = s.accept()
        data = conn.recv(1024)
        
        if not data: 
            conn.close()
            break
        command = data.decode()
        
        game.move(command)
        
        map = game.print_map()
        
        conn.send(map.encode())