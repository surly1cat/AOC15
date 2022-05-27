import hashlib
with open('input.txt') as f:
    key = f.readline()

i = 0
while not hashlib.md5(((key + str(i)).encode())).hexdigest()[:5] == '00000':
    i += 1
with open('output1.txt', 'w') as n:
    n.write(str(i))
