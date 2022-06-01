from itertools import permutations


with open('input.txt', 'r') as f:
    lines = f.readlines()


array = []
for line in lines:
    line = line.replace(' to ', ',')
    line = line.replace(' = ', ',')
    line = line.strip()
    array.append(line.split(','))

array_city = []
for i in range(len(array)):
    if array[i][0] not in array_city:
        array_city.append(array[i][0])
    if array[i][1] not in array_city:
        array_city.append(array[i][1])

perm = list(permutations(array_city))
dist_array = []
for element in perm:
    dist = 0
    for i in range(len(array_city)-1):
        for j in range(len(array)):
            if (element[i] == array[j][0] or element[i] == array[j][1]) and (element[i+1] == array[j][0] or element[i+1] == array[j][1]):
                dist += int(array[j][2])
    dist_array.append(dist)

    if dist <= max(dist_array):
        max_way = element

with open('output2.txt', 'w') as f:
    f.write(str(max(dist_array)))

