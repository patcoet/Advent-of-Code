tiles = []

class Tile:
  def __init__(self, id_, content):
    self.id = id_
    self.content = content
    self.size = max(self.content.keys(), key=lambda x: x[0])[0]

  def __str__(self):
    return f"{self.id}"

  def __repr__(self):
    return str(self)

  def rotate(self):
    tmp = self.content.copy()
    for key in self.content.keys():
      x, y = key
      tmp[(self.size-y, x)] = self.content[(x, y)]
    self.content = tmp

  def hflip(self):
    tmp = self.content.copy()
    for key in self.content.keys():
      x, y = key
      tmp[(self.size-x, y)] = self.content[(x, y)]
    self.content = tmp

  def vflip(self):
    tmp = self.content.copy()
    for key in self.content.keys():
      x, y = key
      tmp[(x, self.size-y)] = self.content[(x, y)]
    self.content = tmp

  def tside(self):
    return [self.content[(x, y)] for (x, y) in self.content.keys() if y == 0]

  def rside(self):
    return [self.content[(x, y)] for (x, y) in self.content.keys() if x == self.size]

  def bside(self):
    return [self.content[(x, y)] for (x, y) in self.content.keys() if y == self.size]

  def lside(self):
    return [self.content[(x, y)] for (x, y) in self.content.keys() if x == 0]

  def sides(self):
    return (self.tside(), self.rside(), self.bside(), self.lside())

  def shave(self):
    tmp = {}
    for x in range(1, self.size):
      for y in range(1, self.size):
        tmp[(x-1, y-1)] = self.content[(x, y)]
    self.content = tmp
    self.size -= 1

# Rotate and flip other_tile until it matches tile's specified side; return None if no match
def match(tile, other_tile, tile_side):
  if tile_side == "top":
    for n in range(12):
      if other_tile.bside() == tile.tside():
        return other_tile
      other_tile.rotate()
      if n == 3:
        other_tile.hflip()
      if n == 7:
        other_tile.vflip()
  elif tile_side == "right":
    for n in range(12):
      if other_tile.lside() == tile.rside():
        return other_tile
      other_tile.rotate()
      if n == 3:
        other_tile.hflip()
      if n == 7:
        other_tile.vflip()
  elif tile_side == "bottom":
    for n in range(12):
      if other_tile.tside() == tile.bside():
        return other_tile
      other_tile.rotate()
      if n == 3:
        other_tile.hflip()
      if n == 7:
        other_tile.vflip()
  elif tile_side == "left":
    for n in range(12):
      if other_tile.rside() == tile.lside():
        return other_tile
      other_tile.rotate()
      if n == 3:
        other_tile.hflip()
      if n == 7:
        other_tile.vflip()

  return False

with open("input.txt") as file:
  curr_tile = []
  curr_id = 0

  for line in file:
    if "Tile" in line:
      curr_id = int(line.strip().split(" ")[1][:-1])
      curr_content = {}
      for y in range(len(curr_line := file.readline().strip())):
        for x in range(len(curr_line)):
          curr_content[(x, y)] = curr_line[x]
        curr_line = file.readline().strip()
      tiles.append(Tile(curr_id, curr_content))

def pprint1(tile):
  for yy in range(10):
    print("".join([tile.content[(x, y)] for (x, y) in tile.content.keys() if y == yy]))

import math
def pprint(tiles):
  tiles_per_side = int(math.sqrt(len(tiles)))
  offset = 0
  for line in range(tiles[0].size * tiles_per_side):
    yy = line % tiles[0].size
    if line >= tiles[0].size and yy == 0:
      offset += tiles_per_side
    s = ""

    for n in range(tiles_per_side):
      s += "".join([tiles[n+offset].content[(x, y)] for (x, y) in tiles[n+offset].content.keys() if y == yy])
    print(s)

def combine(tiles):
  tiles_per_side = int(math.sqrt(len(tiles)))
  offset = 0
  lines = []
  tmp = {}
  for line in range(tiles[0].size * tiles_per_side):
    yy = line % tiles[0].size
    if line >= tiles[0].size and yy == 0:
      offset += tiles_per_side
    s = ""

    for n in range(tiles_per_side):
      s += "".join([tiles[n+offset].content[(x, y)] for (x, y) in tiles[n+offset].content.keys() if y == yy])
    for x in range(len(s)):
      tmp[(line, x)] = s[x]
    lines.append(s)
  return tmp

sorted_tiles = []

# Find a corner tile
for tile in tiles:
  matching_tiles = 0
  for side in tile.sides():
    matched = False
    for other_tile in filter(lambda x: x != tile, tiles):
      if any([side == other_side for other_side in other_tile.sides()]):
        matched = True
      other_tile.hflip()
      if any([side == other_side for other_side in other_tile.sides()]):
        matched = True
      other_tile.vflip()
      if any([side == other_side for other_side in other_tile.sides()]):
        matched = True

    if matched:
      matching_tiles += 1
  if matching_tiles == 2:
    sorted_tiles.append(tile)
    break

# Fill out the rest of the first row
for tile in sorted_tiles:
  for other_tile in filter(lambda x: x not in sorted_tiles, tiles):
    if match(tile, other_tile, "right"):
      sorted_tiles.append(other_tile)
      break

# Add the first piece of the second row, flipping the first row first if needed
added = False
for other_tile in filter(lambda x: x not in sorted_tiles, tiles):
  if match(sorted_tiles[0], other_tile, "bottom"):
    sorted_tiles.append(other_tile)
    added = True
    break
if not added:
  for tile in sorted_tiles:
    tile.vflip()
  for other_tile in filter(lambda x: x not in sorted_tiles, tiles):
    if match(sorted_tiles[0], other_tile, "bottom"):
      sorted_tiles.append(other_tile)
      break

# Add the rest of the pieces
for tile in sorted_tiles:
  for other_tile in filter(lambda x: x not in sorted_tiles, tiles):
    if match(tile, other_tile, "bottom"):
      sorted_tiles.append(other_tile)

# pprint(sorted_tiles)

for tile in sorted_tiles:
  tile.shave()
  # print(tile.content)

# print(len(sorted_tiles))
# print(combine(sorted_tiles))

# combined = combine(sorted_tiles)

def pprintc(coords):
  side_length = int(math.sqrt(len(coords.keys())))
  for yy in range(side_length):
    print("".join([coords[(x, y)] for (x, y) in sorted(coords.keys()) if y == yy]))

def rotate(coords):
  tmp = {}
  side_length = int(math.sqrt(len(coords.keys()))) - 1
  for key in coords.keys():
    x, y = key
    tmp[(side_length - y, x)] = coords[(x, y)]
  return tmp

def hflip(coords):
  tmp = {}
  side_length = int(math.sqrt(len(coords.keys()))) - 1
  for key in coords.keys():
    x, y = key
    tmp[(side_length-x, y)] = coords[(x, y)]
  return tmp

def hflip(coords):
  tmp = {}
  side_length = int(math.sqrt(len(coords.keys()))) - 1
  for key in coords.keys():
    x, y = key
    tmp[(x, side_length-y)] = coords[(x, y)]
  return tmp


combined = combine(sorted_tiles)
# pprintc(combined)
# print()
# rotated = rotate(combined)
# pprintc(rotated)

# print(combined)

monster_count = 0

pprintc(combined)

combined = rotate(combined)
combined = rotate(combined)

for yy in range(int(math.sqrt(len(combined.keys()))) - 2):
  # l1 = combined[y]
  # l2 = combined[y+1]
  # l3 = combined[y+2]
  l1 = "".join([combined[(x, y)] for (x, y) in combined.keys() if y == yy])
  l2 = "".join([combined[(x, y)] for (x, y) in combined.keys() if y == yy+1])
  l3 = "".join([combined[(x, y)] for (x, y) in combined.keys() if y == yy+2])
  for x in range(len(l1) - 18):
    if "#" == l1[18+x] == l2[0+x] == l2[5+x] == l2[6+x] == l2[11+x] == l2[12+x] == l2[17+x] == l2[18+x] == l2[19+x] == l3[1+x] == l3[4+x] == l3[7+x] == l3[10+x] == l3[13+x] == l3[16+x]:
      print(yy)
      monster_count += 1

print("monsters", monster_count)

print(len([char for char in combined.values() if char == "#"]) - monster_count*15)


# print(len([x for x in "".join(combined) if x == "#"]) - 15*monster_count)
  # def rotate(self):
  #   tmp = self.content.copy()
  #   for key in self.content.keys():
  #     x, y = key
  #     tmp[(self.size-y, x)] = self.content[(x, y)]
  #   self.content = tmp

  # def hflip(self):
  #   tmp = self.content.copy()
  #   for key in self.content.keys():
  #     x, y = key
  #     tmp[(self.size-x, y)] = self.content[(x, y)]
  #   self.content = tmp

  # def vflip(self):
  #   tmp = self.content.copy()
  #   for key in self.content.keys():
  #     x, y = key
  #     tmp[(x, self.size-y)] = self.content[(x, y)]
  #   self.content = tmp


#1954 high