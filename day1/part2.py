with open("input.txt") as f:
    line = f.read()

up = 0
down = 0
for i in range(len(line)):
    if line[i] == '(':
        up += 1
    else:
        down += 1
    if up - down == -1:
        with open("output2.txt", 'w') as a:
            a.write(str(i + 1))  # берем в учет, что i начинается с 1
        break
