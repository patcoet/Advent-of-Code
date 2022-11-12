import re

counters = [0] * 10

with open('input') as file:
    for n in re.findall('(\d+),?', file.readline()):
        counters[int(n) + 1] += 1

for _ in range(256):
    for i in range(len(counters) - 1):
        counters[i] = counters[i + 1]
    counters[-1] = 0

    if counters[0] > 0:
        counters[7] += counters[0]
        counters[9] += counters[0]
        counters[0] = 0

print(sum(counters))
