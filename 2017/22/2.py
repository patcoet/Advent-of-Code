def read(filename):
  grid = {}
  with open(filename) as file:
    y = 0
    for line in file:
      line = line.strip()
      for x in range(len(line)):
        grid[(x, y)] = (line[x] == '#') * 2 # 2 if infected, 0 if clean
      y = y + 1
  return grid, (y//2, y//2)

class Carrier:
  def __init__(self, position, direction, infect_count=0):
    self.position = position
    self.direction = direction
    self.infect_count = infect_count

  def burst(self, grid):
    if self.position not in grid.keys():
      grid[self.position] = 0
    node_status = grid[self.position]

    if node_status == 0:   # Clean
      self.direction = (self.direction - 1) % 4
    elif node_status == 1: # Weakened
      self.direction = self.direction
      self.infect_count += 1
    elif node_status == 2: # Infected
      self.direction = (self.direction + 1) % 4
    else:                  # Flagged
      self.direction = (self.direction + 2) % 4

    grid[self.position] = (grid[self.position] + 1) % 4

    x, y = self.position
    if self.direction == 0:   # North
      y -= 1
    elif self.direction == 1: # East
      x += 1
    elif self.direction == 2: # South
      y += 1
    else:                     # West
      x -= 1
    self.position = (x, y)

    return grid

grid, carrier_pos = read('input.txt')
carrier = Carrier(carrier_pos, 0)
for i in range(10000000):
  grid = carrier.burst(grid)

print(carrier.infect_count)
