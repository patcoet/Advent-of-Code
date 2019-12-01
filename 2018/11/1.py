serial_number = 1955

def power_level_of_cell(x, y):
  rack_id = x + 10
  power_level = rack_id * y
  power_level = power_level + serial_number
  power_level = power_level * rack_id
  hundreds_digit = (power_level % 1000) // 100
  return hundreds_digit - 5

def neighbors_of(x0, y0):
  if x0 == 1 or x0 == 300 or y0 == 1 or y0 == 300:
    return False
  else:
    return [[x, y] for x in range(x0-1, x0+2) for y in range(y0-1, y0+2) if [x, y] != [x0, y0]]

grid = {}
for x in range(1, 301):
  grid[x] = {}
  for y in range(1, 301):
    grid[x][y] = power_level_of_cell(x, y)

max_square_power_level = 0
max_square_top_left = (0, 0)

for x in range(1, 301):
  for y in range(1, 301):
    neighbors = neighbors_of(x, y)
    if neighbors:
      square_power_level = grid[x][y] + sum([grid[x][y] for x,y in neighbors])
      if square_power_level > max_square_power_level:
        max_square_power_level = square_power_level
        max_square_top_left = (x-1, y-1)

print(max_square_top_left)