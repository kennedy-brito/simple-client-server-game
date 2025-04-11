map = [[0 for i in range(10)] for j in range(10)]

x = 3
y = 3

map[x][y] = 1

def print_map():
    text = ""
    for i in map:
        for j in i:
            text += f"{j} "
        text += "\n"
    return text

def move(input):
    global x, y
    map[x][y] = 0
    if input == "w" and x > 0:
        x -= 1
    if input == "s" and x < 9:
        x += 1
    if input == "a" and y > 0:
        y -= 1
    if input == "d" and y < 9:
        y += 1
    map[x][y] = 1

