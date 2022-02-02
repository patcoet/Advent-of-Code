# Day 10: Monitoring Station
# Determine which asteroid will be the 200th to be vaporized by a rotating laser.
# Idea: Get a list of asteroids in line of sight of the station, and compute a list of them in clockwise order from 12. Iterate through and repopulate the list until reaching the target number.
import math

def coords_between(coord1, coord2):
  x1, y1 = coord1
  x2, y2 = coord2
  if x2 < x1 and y2 < y1:
    x1, y1 = coord2
    x2, y2 = coord1

  dx = x2 - x1
  dy = y2 - y1

  nx = dx / max(abs(dx), abs(dy))
  ny = dy / max(abs(dx), abs(dy))

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

# Given an origin and a list of asteroid coordinates, return a list of asteroids that are in line of sight from the origin:
def seen_from(org, coords):
  return set([coord for coord in coords if coord != org and coords_between(org, coord).isdisjoint(coords)])

# Given two coordinates, return the angle between them, growing clockwise from 0.
def angle_between(coord1, coord2):
  dx = coord1[0] - coord2[0]
  dy = coord1[1] - coord2[1]

  atan2 = math.degrees(math.atan2(dx, dy)) # Going clockwise from north, math.atan2 returns 0 to -180, then 180 to 0.

  if atan2 > 0:                            # This makes it go from 0 to -360,
    atan2 = -360 + atan2

  atan2 = -atan2                           # and then just invert.

  return atan2



ast_map = {}
with open("input.txt") as file:
  for y, line in enumerate(file):
    for x, char in enumerate(line.strip()):
      ast_map[(x, y)] = char
asteroid_coords = set([coord for coord in ast_map if ast_map[coord] == "#"])

station_location = max(asteroid_coords, key=lambda x: len(seen_from(x, asteroid_coords)))

vaporized_asteroids = []
while len(vaporized_asteroids) < 200:
  seen_asteroids_sorted = sorted(seen_from(station_location, asteroid_coords), key=lambda x: angle_between(station_location, x))
  asteroid_coords = asteroid_coords.difference(seen_asteroids_sorted)

  while len(seen_asteroids_sorted) > 0:
    vaporized_asteroids.append(seen_asteroids_sorted.pop(0)) # For performance we shouldn't build this whole list (which will also usually go a bit beyond 200 in length), but whatever.

last_vaporized = vaporized_asteroids[199]

print(f"The 200th asteroid to be vaporized is at {last_vaporized}. x*100 + y = {last_vaporized[0]*100 + last_vaporized[1]}.")
