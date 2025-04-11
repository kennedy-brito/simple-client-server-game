from server import server
from client import client
from threading import Thread
from threading import Condition

HOST = ''
PORT = 5007

if __name__ == "__main__":
  
  server_thread = Thread(None, server, args=[HOST, PORT])
  server_thread.start()
  
  client(HOST, PORT)