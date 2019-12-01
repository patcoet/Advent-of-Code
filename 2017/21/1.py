import math

class Rule:
  def __init__(self, inpt, outpt):
    self.inpt = inpt
    self.outpt = outpt

  def __str__(self):
    return self.inpt + " => " + self.outpt

  def __repr__(self):
    return str(self)

  def match(self, pattern):
    # print("match?:", self.inpt, pattern)
    patterns = [pattern, rotate(pattern), rotate(rotate(pattern)), rotate(rotate(rotate(pattern))),
                flip(pattern), rotate(flip(pattern)), rotate(rotate(flip(pattern))), rotate(rotate(rotate(flip(pattern))))]
    for p in patterns:
      if p == self.inpt:
        # print("Matched:", pattern, "=", self.inpt, "=>", self.outpt)
        return True, self.outpt
    return False, pattern

def read(filename):
  rules = []
  with open(filename) as file:
    for line in file:
      parts = line.split('=>')
      inpt = parts[0].strip()
      outpt = parts[1].strip()
      rules.append(Rule(inpt, outpt))
  return rules

# Given a 2x2 or 3x3 grid, rotate it 90 degrees clockwise
def rotate(grid):
  rows = grid.split('/')
  if len(rows) == 2:
    return rows[1][0] + rows[0][0] + '/' + rows[1][1] + rows[0][1]
  elif len(rows) == 3:
    return rows[2][0] + rows[1][0] + rows[0][0] + '/' + rows[2][1] + rows[1][1] + rows[0][1] + '/' + rows[2][2] + rows[1][2] + rows[0][2]

# Given a 2x2 or 3x3 grid, flip it vertically
def flip(grid):
  rows = grid.split('/')
  rows = rows[::-1]
  return '/'.join(rows)

# Given a grid of size nxn, return a list of 2x2 grids if n is divisible by 2 or 3x3 if 3
def divide(grid):
  # print("Dividing grid:", grid)
  rows = grid.split('/')
  result = []
  # print("rows:", rows)
  if len(rows) < 4:
    result.append(grid)
  elif len(rows) % 2 == 0:
    while rows != []:
      for i in range(0, len(rows[0]), 2):
        result.append(rows[0][i:i+2] + '/' + rows[1][i:i+2])
      rows.pop(0)
      rows.pop(0)
  else:
    while rows != []:
      for i in range(0, len(rows[0]), 3):
        result.append(rows[0][i:i+3] + '/' + rows[1][i:i+3] + '/' + rows[2][i:i+3])
      rows.pop(0)
      rows.pop(0)
      rows.pop(0)
  # print("Divide result:", result)
  return result

def join_subgrids(subgrids):
  # print("Joining grids:", subgrids)
  grid_size = int(math.sqrt(len(subgrids)))
  lines = []
  if len(subgrids) == 1:
    # print("Join result:", subgrids[0])
    return subgrids[0]
  for i in range(0, len(subgrids), grid_size):
    subs = subgrids[i:i+grid_size]
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    for sub in subs:
      line1 = line1 + sub.split('/')[0]
      line2 = line2 + sub.split('/')[1]
      if len(sub.split('/')) > 2:
        line3 = line3 + sub.split('/')[2]
      if len(sub.split('/')) > 3:
        line4 = line4 + sub.split('/')[3]
    lines.append(line1)
    lines.append(line2)
    if line3 != "":
      lines.append(line3)
    if line4 != "":
      lines.append(line4)
  # print("Join result:", '/'.join(lines))
  return '/'.join(lines)

def iterate(rules, iterations):
  grid = ".#./..#/###"
  for i in range(iterations):
    subgrids = divide(grid)
    for j in range(len(subgrids)):
      subgrid = subgrids[j]
      for rule in rules:
        matched, result = rule.match(subgrid)
        if matched:
          subgrids[j] = result
          break
    grid = join_subgrids(subgrids)
  return sum([char == '#' for char in grid])

rules = read('input.txt')
print(iterate(rules, 5))
