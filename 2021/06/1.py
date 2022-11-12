import re

timers = []

with open('input') as file:
    timers = [int(n) for n in re.findall('(\d+),?', file.readline())]

for _ in range(80):
    timers = [x-1 for x in timers]
    for i, timer in enumerate(timers):
        if timer == -1:
            timers[i] = 6
            timers.append(8)

print(len(timers))
