with open('input.txt') as f:
    total = 0
    for line in f:
        size = [int(i) for i in line[:-1].split('x')]
        size.sort()
        total += 2 * size[0] * size[1] + 2 * size[1] * size[2] + 2 * size[0] * size[2] + size[0] * size[1]
    with open('output1', 'w') as a:
        a.write(str(total))
