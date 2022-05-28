with open('input.txt') as f:
    list = f.readlines()
    dictionary = {}
    while list:
        del_elements = []
        for i in range(len(list)):
            line = list[i]
            data = line.split()
            if len(data) == 3 and data[0].isdigit():
                dictionary[data[2]] = int(data[0])
                del_elements.append(list[i])
            elif len(data) == 3 and data[0] in dictionary:
                dictionary[data[2]] = dictionary[data[0]]
                del_elements.append(list[i])
                dictionary[data[2]]
            elif len(data) == 4 and data[1] in dictionary:
                dictionary[data[3]] = ~ dictionary[data[1]]
                del_elements.append(list[i])
                dictionary[data[3]]
            else:
                if data[1] == 'AND':
                    if data[0] in dictionary and data[2] in dictionary:
                        dictionary[data[4]] = dictionary[data[0]] & dictionary[data[2]]
                        del_elements.append(list[i])
                        dictionary[data[4]]
                    elif data[0].isdigit() and data[2] in dictionary:
                        dictionary[data[4]] = int(data[0]) & dictionary[data[2]]
                        del_elements.append(list[i])
                        dictionary[data[4]]
                elif data[1] == 'OR':
                    if data[0] in dictionary and data[2] in dictionary:
                        dictionary[data[4]] = dictionary[data[0]] | dictionary[data[2]]
                        del_elements.append(list[i])
                        dictionary[data[4]]
                    elif data[0].isdigit() and data[2] in dictionary:
                        dictionary[data[4]] = int(data[0]) | dictionary[data[2]]
                        del_elements.append(list[i])
                        dictionary[data[4]]
                elif data[1] == 'RSHIFT' and data[0] in dictionary:
                    dictionary[data[4]] = dictionary[data[0]] >> int(data[2])
                    del_elements.append(list[i])
                    dictionary[data[4]]
                elif data[1] == 'LSHIFT' and data[0] in dictionary:
                    dictionary[data[4]] = dictionary[data[0]] << int(data[2])
                    del_elements.append(list[i])
                    dictionary[data[4]]

        for i in del_elements:
            list.remove(i)

with open('output1.txt', 'w') as f:
    f.write(str(dictionary['a']))
