# Day 10: Monitoring Station
# Determine the best asteroid monitoring station on a given map.
# Idea: Draw a line between two coordinates. If at any point the line's x and y coordinates are the same as those of an asteroid, that asteroid blocks line of sight between the coordinates.

def angle_between(coord1, coord2):
  x1, y1 = coord1
  x2, y2 = coord2

  dx = x2 - x1
  dy = y2 - y1

  nx = dx / max(abs(dx), abs(dy))
  ny = dy / max(abs(dx), abs(dy))

  return nx, ny

def coords_between(coord1, coord2):
  x1, y1 = coord1
  x2, y2 = coord2
  if x2 < x1 and y2 < y1:
    x1, y1 = coord2
    x2, y2 = coord1

  nx, ny = angle_between((x1, y1), (x2, y2))

  coords = []
  xx = -1
  yy = -1
  i = 0

  while abs(xx - float(x2)) > 0.0001 or abs(yy - float(y2)) > 0.0001: # This is... not how I'd prefer to do this. But it works!
    xx = x1 + nx*i
    yy = y1 + ny*i

    if abs(xx - int(xx)) < 0.0001 and abs(yy - int(yy)) < 0.0001:
      coords.append((int(xx), int(yy)))
    i += 1

  return set(coords[1:-1])

ast_map = {}
with open("input.txt") as file:
  for y, line in enumerate(file):
    for x, char in enumerate(line.strip()):
      ast_map[(x, y)] = char

asteroid_coords = set(coord for coord in ast_map if ast_map[coord] == "#")

seen_from = {}
for coord in asteroid_coords:
  seen_from[coord] = 0
  for other_coord in asteroid_coords:
    if coord != other_coord:
      coords = coords_between(coord, other_coord)
      if coords.isdisjoint(asteroid_coords):
        seen_from[coord] += 1

best_location = max(seen_from, key=lambda x: seen_from[x])

print(f"The maximum of {seen_from[best_location]} asteroids can be seen from location {best_location}.")