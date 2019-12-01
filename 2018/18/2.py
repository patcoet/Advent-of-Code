area = []

with open('input.txt') as file:
  for line in file:
    area.append(line.strip())

size = len(area)

def neighbors(x, y):
  return [area[xx][yy] for xx in range(x-1, x+2) for yy in range(y-1, y+2) if xx >= 0 and xx < size and yy >= 0 and yy < size and (xx, yy) != (x, y)]


def print_area():
  for y in range(size):
    s = ""
    for x in range(size):
      s = s + area[y][x]
    print(s)
  print()

# print_area()

def tick():
  tmp = []
  for x in range(0, size):
    tmp.append([])
    for y in range(0, size):
      tmp[x].append([])
      cell = area[x][y]
      ns = neighbors(x, y)
      trees = sum([n == '|' for n in ns])
      yards = sum([n == '#' for n in ns])

      if cell == '.' and trees >= 3:
        tmp[x][y] = '|'
      elif cell == '|' and yards >= 3:
        tmp[x][y] = '#'
      elif cell == '#' and not (trees >= 1 and yards >= 1):
        tmp[x][y] = '.'
      else:
        tmp[x][y] = cell
  return tmp

prev_totals = {}
not_done = True
last = -1

trees = sum([sum([1 * cell == '|' for cell in row]) for row in area])
yards = sum([sum([1 * cell == '#' for cell in row]) for row in area])
points = trees * yards
print(points)

for i in range(1, 500):
  if not_done:
    area = tick()
    trees = sum([sum([1 * cell == '|' for cell in row]) for row in area])
    yards = sum([sum([1 * cell == '#' for cell in row]) for row in area])
    points = trees * yards
    print(i, points)
    # if points in prev_totals.values() and last in prev_totals.values():
    # for k, v in prev_totals.items():
    #   if v == points and prev_totals[k-1] == last:
    #     cycle_start = k - (i - k)
    #     cycle_length = i - k
    #     print(i, k, cycle_start, cycle_length)
    #     print((1000000000 - cycle_start) % cycle_length)
    #     print(prev_totals[cycle_start + 9])
    #     # diff = i - k
    #     # for j in range(k, i):
    #     #   print(prev_totals[j])
    #     # print(points)
    #     not_done = False
    #     break
    last = points
    prev_totals[i] = points



# for row in area:

# 224000 too low
# 233772 too high
# 233058
# print_area()
# 429 is the last tick outside the cycle
# 430 == 458, 431 == 459, ...