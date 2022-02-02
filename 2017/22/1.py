def read(filename):
  grid = {}
  with open(filename) as file:
    y = 0
    for line in file:
      line = line.strip()
      for x in range(len(line)):
        grid[(x, y)] = line[x] == '#' # True if infected, False otherwise
      y = y + 1
  return grid, (y//2, y//2)

class Carrier:
  def __init__(self, position, direction, infect_count=0):
    self.position = position
    self.direction = direction
    self.infect_count = infect_count

  def burst(self, grid):
    # print("Bursting at position:", self.position)
    if self.position not in grid.keys():
      grid[self.position] = False
    node_is_infected = grid[self.position]
    if node_is_infected:
      # print("Saw infected node")
      self.direction = (self.direction + 1) % 4
    else:
      # print("Saw clean node")
      self.direction = (self.direction - 1) % 4
      self.infect_count += 1

    grid[self.position] = not node_is_infected

    x, y = self.position
    if self.direction == 0:   # North
      # print("Moving north")
      y -= 1
    elif self.direction == 1: # East
      # print("Moving east")
      x += 1
    elif self.direction == 2: # South
      # print("Moving south")
      y += 1
    else:                     # West
      # print("Moving west")
      x -= 1
    self.position = (x, y)

    return grid

grid, carrier_pos = read('input.txt')
carrier = Carrier(carrier_pos, 0)
# print(carrier_pos)

for i in range(10000):
  grid = carrier.burst(grid)

print(carrier.infect_count)
