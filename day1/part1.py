with open("input.txt") as f:
    line = f.read()
    with open("output1.txt", 'w') as a:
        a.write(str(line.count('(') - line.count(')')))




