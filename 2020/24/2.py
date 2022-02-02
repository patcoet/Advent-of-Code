instructions = []

with open("input.txt") as file:
  for line in file:
    i = 0
    instruction = []
    while i < len(line.strip()):
      c1 = line[i]
      c2 = line[i:i+2]

      if c1 == "e":
        n = (2, 0)
      elif c2 == "se":
        n = (1, 1)
      elif c2 == "sw":
        n = (-1, 1)
      elif c1 == "w":
        n = (-2, 0)
      elif c2 == "nw":
        n = (-1, -1)
      else:
        n = (1, -1)

      instruction.append(n)

      if line[i] == "e" or line[i] == "w":
        i += 1
      else:
        i += 2
    instructions.append(instruction)

tiles = {} # tile[(x, y)] = n: tile at (x, y) has been flipped n times

# This is easier than adding tiles dynamically and produces the right answer for my input:
for x in range(-200, 200):
  for y in range(-200, 200):
    tiles[(x, y)] = 0

for instruction in instructions:
  coord = (0, 0)
  for step in instruction:
    x0, y0 = coord
    x, y = step
    coord = (x0+x, y0+y)
  if coord not in tiles.keys():
    tiles[coord] = 1
  else:
    tiles[coord] += 1

for turn in range(100):
  print(turn)
  tmp = tiles.copy()
  for (coord, flipped) in tiles.items():
    x0, y0 = coord
    nx = [-1, 1, -1, 1, -2, 2]
    ny = [-1, -1, 1, 1, 0, 0]
    neighbor_coords = [(x0 + nx[n], y0 + ny[n]) for n in range(len(nx))]

    black_neighbors = 0
    for neighbor_coord in neighbor_coords:
      if neighbor_coord in tiles.keys() and tiles[neighbor_coord] % 2 == 1:
        black_neighbors += 1

    if flipped % 2 == 0 and black_neighbors == 2: # tile is white
      tmp[coord] = 1
    elif flipped % 2 == 1 and (black_neighbors == 0 or black_neighbors > 2):
      tmp[coord] = 0

  tiles = tmp

print(len([x for x in tiles.values() if x % 2 == 1]))