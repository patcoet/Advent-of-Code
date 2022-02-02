space = {}

with open("input.txt") as file:
  y = 0
  for line in file:
    x = 0
    for char in line.strip():
      space[(x, y, 0)] = char
      x += 1
    y += 1

def tick(space):
  space2 = space.copy()

  for coord in space.keys():
    pm = [(c-1, c, c+1) for c in coord]
    for neighbor_coord in [(x, y, z) for x in pm[0] for y in pm[1] for z in pm[2] if (x, y, z) != coord]:
      if neighbor_coord not in space.keys():
        space2[neighbor_coord] = "."

  for coord in space2.keys():
    active_neighbors = 0

    pm = [(c-1, c, c+1) for c in coord]
    for neighbor_coord in [(x, y, z) for x in pm[0] for y in pm[1] for z in pm[2] if (x, y, z) != coord]:
      if neighbor_coord in space.keys() and space[neighbor_coord] == "#":
        active_neighbors += 1

    if space2[coord] == "#" and not (active_neighbors == 2 or active_neighbors == 3):
      space2[coord] = "."
    elif space2[coord] == "." and active_neighbors == 3:
      space2[coord] = "#"

  return space2

def pprint(space):
  xs = [a[0] for a in space.keys()]
  ys = [a[1] for a in space.keys()]
  zs = [a[2] for a in space.keys()]
  for z in range(min(zs), max(zs)+1):
    print(f"z={z}")
    for y in range(min(ys), max(ys)+1):
      line = ""
      for x in range(min(xs), max(xs)+1):
        line += space[(x, y, z)]
      print(line)
    print()

for cycle in range(6):
  # print(f"Cycle #{cycle}")
  # pprint(space)
  space = tick(space)

print(len([x for x in space.values() if x == "#"]))

