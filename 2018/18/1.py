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

for i in range(10):
  area = tick()

trees = sum([sum([1 * cell == '|' for cell in row]) for row in area])
yards = sum([sum([1 * cell == '#' for cell in row]) for row in area])

print(trees * yards)