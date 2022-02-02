tracks = []
with open('input.txt') as file:
  for line in file:
    tracks.append(line.strip('\n'))

class Cart:
  def __init__(self, x, y, direction, moved_this_turn=False, previous_turn=0):
    self.x = x
    self.y = y
    self.direction = direction # 0 = ^, 1 = >, 2 = v, 3 = <
    self.moved_this_turn = moved_this_turn
    self.previous_turn = previous_turn

  def move(self):
    if self.moved_this_turn:
      return False

    if self.direction == 0:
      self.y = self.y - 1
    elif self.direction == 1:
      self.x = self.x + 1
    elif self.direction == 2:
      self.y = self.y + 1
    elif self.direction == 3:
      self.x = self.x - 1

    curr_track_symbol = tracks[self.y][self.x]

    if curr_track_symbol == '/':
      if self.direction == 0 or self.direction == 2:
        self.direction = (self.direction + 1) % 4
      else:
        self.direction = (self.direction - 1) % 4
    elif curr_track_symbol == '\\':
      if self.direction == 0 or self.direction == 2:
        self.direction = (self.direction - 1) % 4
      else:
        self.direction = (self.direction + 1) % 4
    elif curr_track_symbol == '+':
      if self.previous_turn == 0: # If previous was right, turn left
        self.direction = (self.direction - 1) % 4
      elif self.previous_turn == 1: # If previous was left, go straight
        pass
      elif self.previous_turn == 2: # If previous was straight, turn right
        self.direction = (self.direction + 1) % 4
      self.previous_turn = (self.previous_turn + 1) % 3

    self.moved_this_turn = True

carts = []

for y in range(len(tracks)):
  for x in range(len(tracks[y])):
    symbol = tracks[y][x]
    if symbol == '^':
      carts.append(Cart(x, y, 0))
      tracks[y] = tracks[y][:x] + '|' + tracks[y][x+1:]
    elif symbol == '>':
      carts.append(Cart(x, y, 1))
      tracks[y] = tracks[y][:x] + '-' + tracks[y][x+1:]
    elif symbol == 'v':
      carts.append(Cart(x, y, 2))
      tracks[y] = tracks[y][:x] + '|' + tracks[y][x+1:]
    elif symbol == '<':
      carts.append(Cart(x, y, 3))
      tracks[y] = tracks[y][:x] + '-' + tracks[y][x+1:]

def carts_at(x, y):
  result = []
  for cart in carts:
    if cart.x == x and cart.y == y:
      result.append(cart)
  return result

while len(carts) > 1:
  for y in range(len(tracks)):
    for x in range(len(tracks[y])):
      carts_at_position = carts_at(x, y)
      if len(carts_at_position) == 1:
        carts_at_position[0].move()
      elif len(carts_at_position) > 1:
        print("Crash:", x, y)
        for c in carts_at_position:
          carts.remove(c)

  for cart in carts:
    cart.moved_this_turn = False

print("Remaining cart at:", carts[0].x, carts[0].y)
