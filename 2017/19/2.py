area_map = {}

class Packet:
  def __init__(self, position, direction, seen_letters=[]):
    self.position = position
    self.direction = direction
    self.seen_letters = seen_letters

  def __str__(self):
    return str(self.position) + ":" + str(self.direction) + ":" + str(self.seen_letters)

  def move(self):
    self.position = (self.position[0] + self.direction[0], self.position[1] + self.direction[1])
    symbol = area_map[self.position]
    if symbol == ' ':
      return -1
    if symbol != '-' and symbol != '|' and symbol != '+':
      self.seen_letters.append(symbol)
    if symbol == '+':
      x, y = self.position
      if self.direction == (0, -1) or self.direction == (0, 1):
        for direction in [(x-1, y), (x+1, y)]:
          if area_map[direction] != ' ':
            self.direction = (direction[0] - x, direction[1] - y)
      elif self.direction == (-1, 0) or self.direction == (1, 0):
        for direction in [(x, y-1), (x, y+1)]:
          if area_map[direction] != ' ':
            self.direction = (direction[0] - x, direction[1] - y)

def read(filename):
  width = 0
  with open(filename) as file:
    y = 0
    for line in file:
      for x in range(len(line)):
        if line[x] != '\n':
          area_map[(x, y)] = line[x]
          if y == 0:
            width = width + 1
      y = y + 1
  return width

width = read('input.txt')
for x in range(width):
  if area_map[(x, 0)] == '|':
    start_x = x

packet = Packet((start_x, 0), (0, 1))
steps = 0
while True:
  steps = steps + 1
  if packet.move() == -1:
    break

print(''.join(packet.seen_letters))
print(steps)
