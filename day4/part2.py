import hashlib as hl

with open("input.txt", 'r') as f:
    line = f.readline()
    for i in range(10000000):
        byte_line = line + str(i)
        byte_line = byte_line.encode('utf-8')
        hash_object = hl.md5(byte_line)
        hash_MD5 = hash_object.hexdigest()
        if hash_MD5[0:6] == '000000':
            answer = i
            break
with open('output2.txt', 'w') as f:
    f.write(str(answer))
