reservoir = {}

with open('input.txt') as file:
  for line in file:
    p1 = line[2:line.find(',')]
    p2 = line[line.find('=', 2):].strip('=').strip().split('..')
    num1 = int(p1)
    num2 = int(p2[0])
    num3 = int(p2[1])
    if line[0] == 'x':
      for y in range(num2, num3+1):
        reservoir[(num1, y)] = '#'
    else:
      for x in range(num2, num3+1):
        reservoir[(x, num1)] = '#'
  reservoir[(500, 0)] = '+'

x0 = 999
x1 = -999
y0 = 999
y1 = -999
for coord in reservoir.keys():
  x, y = coord
  x0 = min(x0, x)
  x1 = max(x1, x)
  y0 = min(y0, y)
  y1 = max(y1, y)

x0 = x0 - 1
x1 = x1 + 1

def res(x, y):
  if (x, y) in reservoir.keys():
    return reservoir[(x, y)]
  else:
    reservoir[(x, y)] = '.'
    return '.'

def print_reservoir():
  # for y in range(0, 20):
  for y in range(y0, y1+1):
    s = str(y).ljust(10)
    for x in range(x0, x1+1):
      s = s + res(x, y)
    print(s)
  print()

start_x = 500
start_y = 0

def liquid_count():
  print(x0, x1, y0, y1)
  total = 0
  for x in range(x0, x1+1):
    for y in range(1, y1+1):
      total = total + 1 * (res(x, y) == '|' or res(x, y) == '~')
  return total

score = 0
went_left_last_time = {}
def drip(x, y):
  global score

  if y > y1:
    return (False, start_x, start_y)
  elif res(x, y) == '+':
    return (False, x, y+1)
  elif res(x, y) == '.':
    above = res(x, y-1)
    if above == '+' or above == '|':
      score = score + 1
      reservoir[(x, y)] = '|'
      return (False, x, y+1)
    for xx in range(x, x0-1, -1):
      if res(xx, y) == '|':
        return (False, xx, y)
      if res(xx, y) == '#':
        for xx in range(x, x1+1):
          if res(xx, y) == '|':
            return (False, xx, y)
  elif res(x, y) == '|':
    below = res(x, y+1)
    if below == '.' or below == '|':
      return (False, x, y+1)
    xx = x
    enclosed_left = False
    xx0 = x1
    xx1 = x0
    for xx in range(x-1, x0-1, -1):
      xx0 = min(xx0, xx)
      if res(xx, y+1) == '.' or res(xx, y+1) == '|':
        enclosed_left = False
        break
      if res(xx, y) == '#':
        enclosed_left = True
        xx0 = xx0+1
        break
    enclosed_right = False
    for xx in range(x+1, x1+1):
      xx1 = max(xx1, xx)
      if res(xx, y+1) == '.' or res(xx, y+1) == '|':
        enclosed_right = False
        break
      if res(xx, y) == '#':
        enclosed_right = True
        xx1 = xx1 - 1
        break
    if enclosed_left and enclosed_right:
      for xx in range(xx0, xx1+1):
        reservoir[(xx, y)] = '~'
      return (False, x, y-1)
    else:
      for xx in range(xx0, xx1+1):
        reservoir[(xx, y)] = '|'
      wl = went_left_last_time[(x, y)] if (x, y) in went_left_last_time.keys() else False
      if (not enclosed_left) and (enclosed_right or not wl):
        went_left_last_time[(x, y)] = True
        return (False, xx0, y)
      else:
        went_left_last_time[(x, y)] = False
        return (False, xx1, y)
  elif res(x, y) == '~':
    return (False, x, y-1)
  elif res(x, y) == '#':
    if res(x, y-1) == '|':
      return (False, x, y-1)

last = -1
while score != last:
  last = score
  for turns in range(200000):
    done, x, y = drip(x, y)
print_reservoir()
print(liquid_count())

# 31889 too high
# 31888 too high

# total = 0
# for y in range(0, y1+1):
#   if any([res(x, y) == '#' for x in range(x0, x1+1)]):
#     total = total + sum([res(x, y) == '|' or res(x, y) == '~' for x in range(x0, x1+1)])
# print(total)

count = 0
for y in range(7, 1898):
  for x in range(x0-100, x1+100):
    if res(x, y) == '|' or res(x, y) == '~':
      count = count + 1

print(count)
#31756 too low