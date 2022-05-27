import re

c = 0


def dup(string):
    prev = '!'
    for i in range(len(string)):
        if string[i] == prev:
            return True
        prev = string[i]


with open('input.txt') as f:
    for line in f:
        line = line[:-1]
        if len(re.findall(r'[aeiou]', line)) >= 3 and dup(line) and not (
                'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line): c += 1

with open('output1.txt', 'w') as n:
    n.write(str(c))
