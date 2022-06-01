with open('input.txt') as f:
    line = f.read()

coord = [0, 0]
visited = []

for i in line:
    if i == '^':
        coord[1] += 1
    elif i == '>':
        coord[0] += 1
    elif i == '<':
        coord[0] -= 1
    elif i == 'v':
        coord[1] -= 1

    if str(coord) not in visited:
        visited.append(str(coord))

with open('output1.txt', 'w') as f:
    f.write(str(len(visited)))

