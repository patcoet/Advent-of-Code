serial_number = 1955

def power_level_of_cell(x, y):
  rack_id = x + 10
  power_level = rack_id * y
  power_level = power_level + serial_number
  power_level = power_level * rack_id
  hundreds_digit = (power_level % 1000) // 100
  return hundreds_digit - 5

def square(x0, y0, size):
  if x0 > 301 - size or y0 > 301 - size:
    return False
  else:
    return [[x, y] for x in range(x0, x0+size) for y in range(y0, y0+size)]

grid = {}
for x in range(1, 301):
  grid[x] = {}
  for y in range(1, 301):
    grid[x][y] = power_level_of_cell(x, y)

max_square_power_level = 0
max_square_top_left = (0, 0, 0)

for x in range(1, 301):
  print(x)
  for y in range(1, 301):
    for s in range(1, 301):
      sq = square(x, y, s)
      if sq:
        square_power_level = sum([grid[x][y] for x,y in sq])
        if square_power_level > max_square_power_level:
          max_square_power_level = square_power_level
          max_square_top_left = (x, y, s)

print(max_square_top_left)
