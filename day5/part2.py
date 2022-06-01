Score = 0

bad_strings = 0
nice_strings = 0

class SomeError(BaseException):
    None

class FinalRaise(BaseException):
    None

with open('input.txt', 'r') as f:
 
    for line in f:
        Score += 1

with open('input.txt', 'r') as f:    
    while True:
        try:
            for line in f:
                for i in range(len(line)-2):
                    if line[i] == line[i+2]:
                        for j in range(len(line)-1):
                            if line.count(line[j]+line[j+1]) > 2:
                                raise FinalRaise()
                            elif line.count(line[j]+line[j+1]) == 2:
                                if 4*line[j] in line:
                                    raise FinalRaise()
                                elif line[j] != line[j+2]:
                                    raise FinalRaise()
                                
                        raise SomeError()
                                        
                            
                raise SomeError()
        except SomeError:
            bad_strings += 1
            if bad_strings + nice_strings == Score:
                break
        except FinalRaise:
            nice_strings += 1
            if bad_strings + nice_strings == Score:
                break

with open('output2.txt', 'w') as f:
    f.write(str(nice_strings))
