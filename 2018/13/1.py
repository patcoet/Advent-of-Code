tracks = []
with open('input.txt') as file:
  for line in file:
    tracks.append(line.strip('\n').strip('#'))

class Cart:
  def __init__(self, x, y, direction, moved_this_turn=False, previous_turn='right'):
    self.x = x
    self.y = y
    self.direction = direction
    self.moved_this_turn = moved_this_turn
    self.previous_turn = previous_turn

  def __repr__(self):
    return str(self)

  def __str__(self):
    return str(self.x) + ',' + str(self.y) + self.direction

  def move(self):
    if self.moved_this_turn:
      return False
    # print(self)
    if self.direction == '^':
      self.x = self.x - 1
    elif self.direction == 'v':
      self.x = self.x + 1
    elif self.direction == '<':
      self.y = self.y - 1
    elif self.direction == '>':
      self.y = self.y + 1
    # print(self)
    if tracks[self.x][self.y] == '/':
      if self.direction == '^':
        self.direction = '>'
      elif self.direction == 'v':
        self.direction = '<'
      elif self.direction == '<':
        self.direction = 'v'
      elif self.direction == '>':
        self.direction = '^'
    elif tracks[self.x][self.y] == '\\':
      if self.direction == '>':
        self.direction = 'v'
      elif self.direction == '<':
        self.direction = '^'
      elif self.direction == '^':
        self.direction = '<'
      elif self.direction == 'v':
        self.direction = '>'
    elif tracks[self.x][self.y] == '+':
      if self.previous_turn == 'left':
        self.previous_turn = 'straight'
      elif self.previous_turn == 'straight':
        self.previous_turn = 'right'
        if self.direction == '<':
          self.direction = '^'
        elif self.direction == '^':
          self.direction = '>'
        elif self.direction == '>':
          self.direction = 'v'
        elif self.direction == 'v':
          self.direction = '<'
      elif self.previous_turn == 'right':
        self.previous_turn = 'left'
        if self.direction == '<':
          self.direction = 'v'
        elif self.direction == '^':
          self.direction = '<'
        elif self.direction == '>':
          self.direction = '^'
        elif self.direction == 'v':
          self.direction = '>'
    self.moved_this_turn = True

carts = []

for x in range(len(tracks)):
  for y in range(len(tracks[x])):
    char = tracks[x][y]
    if char == '^' or char == '<' or char == '>' or char == 'v':
      carts.append(Cart(x, y, char))

for x in range(len(tracks)):
  tracks[x] = tracks[x].replace('^', '|').replace('<', '-').replace('>', '-').replace('v', '|')

def find_cart(x, y):
  result = []
  for cart in carts:
    if cart.x == x and cart.y == y:
      result.append(cart)
  return result

def print_tracks():
  for x in range(len(tracks)):
    row = tracks[x]
    line = ""
    for y in range(len(row)):
      cart = find_cart(x, y)
      # print(x, y, cart)
      if len(cart) == 0:
        l = tracks[x][y]
      elif len(cart) == 1:
        l = cart[0].direction
      else:
        l = 'X'
      line = line + l
    print(line)

no_crashes = True
while no_crashes:
  # print("---")
  for x in range(len(tracks)):
    for y in range(len(tracks[x])):
      cart = find_cart(x, y)
      if len(cart) == 1:
        cart[0].move()
      elif len(cart) > 1:
        print("Crash:", y, x)
        no_crashes = False
  for cart in carts:
    cart.moved_this_turn = False
  # print_tracks()
  # break

# for x in range(len(lines)):
#   for y in range(len(lines[x])):


