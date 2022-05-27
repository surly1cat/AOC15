with open('input.txt') as f:
    line = f.readlines()
    line = line[:-1]


file_symbols = 0
symbols = 0
for i in line:
    file_symbols += len(i)
    string = i[1:-1]
    i = 0
    len_str = len(string)
    while i < len_str:
        if string[i] == '\\':
            if string[i + 1] == 'x':
                i += 3
            else:
                i += 1

        symbols += 1
        i += 1

with open('output1.txt', 'w') as f:
    f.write(str(file_symbols - symbols))
