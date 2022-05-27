import itertools

with open('input.txt') as f:
    line = f.readlines()

location = []
way = {}
for i in range(len(line)):
    string = line[i].split()
    city1, city2 = string[0], string[2]
    distance = int(string[4])
    way[city1 + city2] = distance
    way[city2 + city1] = distance
    location.append(city1)
    location.append(city2)

location = set(location)

short = 100 ** 10
for route in itertools.permutations(location):
    route_length = 0
    for city1, city2 in zip(route[:-1], route[1:]):
        route_length += way[city1 + city2]
    if route_length < short:
        short = route_length

with open('output1.txt', 'w') as f:
    f.write(str(short))
