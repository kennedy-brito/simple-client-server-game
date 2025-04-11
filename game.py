class Game:
    
  def __init__(self):
    self.map = [[0 for i in range(10)] for j in range(10)]
    
    self.x = 3
    self.y = 3
    
    self.map[self.x][self.y] = 1

  def print_map(self):
    text = ""
    for i in self.map:
        for j in i:
            text += f"{j} "
        text += "\n"
    return text

  def move(self, input):
    x = self.x
    y = self.y
    
    self.map[x][y] = 0
    
    if input == "w" and x > 0:
        x -= 1
    if input == "s" and x < 9:
        x += 1
    if input == "a" and y > 0:
        y -= 1
    if input == "d" and y < 9:
        y += 1
    
    self.x = x
    self.y = y
    
    self.map[x][y] = 1
        