import networkx

depth = 11541
target_x = 14
target_y = 778

grid = {}

def geologic_index(coord):
  x, y = coord
  if x == 0 and y == 0:
    return 0
  if x == target_x and y == target_y:
    return 0
  if y == 0:
    return x * 16807
  if x == 0:
    return y * 48271

  return ((grid[(x-1, y)] + depth) % 20183) * ((grid[(x, y-1)] + depth) % 20183)

def erosion_level(coord):
  return (geologic_index(coord) + depth) % 20183

def region_type(coord):
  if erosion_level(coord) % 3 == 0: return 'rocky'
  if erosion_level(coord) % 3 == 1: return 'wet'
  if erosion_level(coord) % 3 == 2: return 'narrow'

for x in range(target_x+1000):
  for y in range(target_y+1000):
    grid[(x, y)] = geologic_index((x, y))

def valid_items(coord):
  terrain = region_type(coord)
  if terrain == 'rocky':
    return ['torch', 'climbing']
  elif terrain == 'wet':
    return ['climbing', 'neither']
  elif terrain == 'narrow':
    return ['torch', 'neither']

def dijk():
  graph = networkx.Graph()
  for y in range(target_y+100):
    for x in range(target_x+100):
      items = valid_items((x, y))
      graph.add_edge((x, y, items[0]), (x, y, items[1]), weight=7) # Add two nodes at (x, y) with a movement cost of 7, for switching equipment
      for neighbor in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
        xx, yy = neighbor
        if 0 <= xx and xx <= target_x+1000 and 0 <= yy and yy <= target_y+1000:
          for item in items:
            if item in valid_items(neighbor):
              graph.add_edge((x, y, item), (xx, yy, item), weight=1) # Add edge between e.g. (x, y) with torch and (x+1, y) with torch
  return networkx.dijkstra_path_length(graph, (0, 0, 'torch'), (target_x, target_y, 'torch'))

print(dijk())
