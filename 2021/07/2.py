import re

positions = []

with open('input') as file:
    positions = [int(x) for x in re.findall('(\d+),?', file.readline())]

costs = []
for n in range(min(positions), max(positions) + 1):
    costs.append(sum([(abs(n - x) * (abs(n - x) + 1)) // 2 for x in positions]))

print([x for x in costs if x == min(costs)][0])
