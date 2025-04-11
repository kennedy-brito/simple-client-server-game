from socket import *

COMMANDS = """
Game Commands:
\tw: North
\ts: South
\ta: West
\td: East
\tc: Quit the game
"""

HOST = ''
PORT = 5007

while True:
  
  # Investigate further:
  #   when i place the socket and the connect outside the loop
  #   the input is not received? i do not understand way this happens
  # How i resolved this?
  #   I placed the socket and connection in the loop
  # Why i think this is bad?
  #   Because i have to recreate the socket AND the connection
  #   I think this is bad for performance
  #   How can i use a continuous connection? Maybe use a protocol different from TCP?
  # link that i used as a reference: https://stackoverflow.com/questions/15958026/getting-errno-9-bad-file-descriptor-in-python-socket
  s = socket(AF_INET, SOCK_STREAM)
  s.connect((HOST, PORT))
  command = input(COMMANDS)
  command = command.lower()

  if command == "c": 
    
    break

  s.send(command.encode())

  data = s.recv(1024)

  print(data.decode())
  s.close()
