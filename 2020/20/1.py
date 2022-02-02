tiles = []

class Tile:
  def __init__(self, id_, content):
    self.id = id_
    self.content = content
    self.size = max(self.content.keys(), key=lambda x: x[0])[0]

  def __str__(self):
    return f"{self.id}:"

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

with open("test1.txt") as file:
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

corner_tiles = []
side_tiles = []
inner_tiles = []
for tile in tiles:
  matching_sides = 0
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
      matching_sides += 1
  if matching_sides == 2:
    corner_tiles.append(tile)
  elif matching_sides == 3:
    side_tiles.append(tile)
  elif matching_sides == 4:
    inner_tiles.append(tile)

def pprint1(tile):
  for yy in range(10):
    print("".join([tile.content[(x, y)] for (x, y) in tile.content.keys() if y == yy]))

import math
def pprint(tiles):
  tiles_per_side = int(math.sqrt(len(tiles)))
  offset = -3
  for line in range(tiles[0].size * tiles_per_side):
    yy = line % tiles[0].size
    if yy == 0:
      offset += tiles_per_side
    s = ""

    for n in range(tiles_per_side):
      s += "".join([tiles[n+offset].content[(x, y)] for (x, y) in tiles[n+offset].content.keys() if y == yy])
    print(s)


