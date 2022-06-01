from re import sub

class Flying_object():
    def __init__(self,velocity, moving_time, stop_time):
        time = 2503
        self.distance = 0
        counter = 0
        switch = 0
        while counter < time:
            if switch == 0:
                if counter + moving_time < time:
                    self.distance += velocity*moving_time
                else:
                    self.distance += velocity*(time-counter)
                counter += moving_time
                switch = 1
            elif switch == 1:
                counter += stop_time
                switch = 0
            

array = []
with open('input.txt','r') as f:
    for line in f:
        line = sub(r'can fly | km/s for| (seconds, but then must rest for)| seconds.', '', line)
        array.append(line.split())

final_array = []
for element in array:
    obj = Flying_object(int(element[1]),int(element[2]),int(element[3]))
    final_array.append(obj.distance)

with open('output1.txt','w') as f:
    f.write(str(max(final_array)))

