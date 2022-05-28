grid = [[False] * 1000 for x in range(1000)]

def move(command, y_begin, x_begin, y_end, x_end):
    if command == 1:
        for x in range(min(x_begin, x_end), max(x_begin, x_end) + 1):
            for y in range(min(y_begin, y_end), max(y_begin, y_end) + 1):
                grid[y][x] = True
    elif command == 2:
        for x in range(min(x_begin, x_end), max(x_begin, x_end) + 1):
            for y in range(min(y_begin, y_end), max(y_begin, y_end) + 1):
                grid[y][x] = False
    elif command == 3:
        for x in range(min(x_begin, x_end), max(x_begin, x_end) + 1):
            for y in range(min(y_begin, y_end), max(y_begin, y_end) + 1):
                grid[y][x] = (grid[y][x] == False)


with open('input.txt') as f:
    for line in f:
        line = line[:-1].replace(' through ', ',')
        if 'turn on' in line:
            y_b, x_b, y_e, x_e = map(int, line[8:].split(','))
            move(1, y_b, x_b, y_e, x_e)
        elif 'turn off' in line:
            y_b, x_b, y_e, x_e = map(int, line[9:].split(','))
            move(2, y_b, x_b, y_e, x_e)
        elif 'toggle' in line:
            y_b, x_b, y_e, x_e = map(int, line[7:].split(','))
            move(3, y_b, x_b, y_e, x_e)
        else:
            print('ERROR')
c = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[j][i]: c += 1
with open('output1.txt', 'w') as f:
    f.write(str(c))
