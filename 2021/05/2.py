import collections
import re

points = collections.defaultdict(int)

with open('input') as file:
  for line in file:
    x1, y1, x2, y2 = map(int, re.findall('(\d+),(\d+) -> (\d+),(\d+)', line)[0])

    if x1 == x2:
      for y in range(min(y1, y2), max(y1, y2) + 1):
        points[(x1, y)] += 1
    elif y1 == y2:
      for x in range(min(x1, x2), max(x1, x2) + 1):
        points[(x, y1)] += 1
    elif abs(x1 - x2) == abs(y1 - y2):
      xs = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
      ys = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
      for p in zip(xs, ys):
        points[p] += 1

print(sum([p > 1 for p in points.values()]))
