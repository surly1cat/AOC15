with open('input.txt') as f:
    line = f.read()

human = line[::2]
robot = line[1::2]
visited = []


def move(line1):
    for i in line1:
        x, y = 0,0
        if i == '^':
            y += 1
        elif i == '>':
            x += 1
        elif i == '<':
            x -= 1
        elif i == 'v':
            y -= 1
        coord = [x, y]
        print(coord)
        if str(coord) not in visited:
            visited.append(str(coord))


move(human)
move(robot)
print(len(visited))
