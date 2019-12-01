coords = []
with open('input.txt') as file:
  for line in file:
    xy = line.strip().split(',')
    coords.append((int(xy[0]), int(xy[1])))

def distance_to_cell(coord, cell):
  (x1, y1) = coord
  (x2, y2) = cell
  dx = abs(x2 - x1)
  dy = abs(y2 - y1)
  manhattan_distance = dx + dy
  return manhattan_distance

leftest = min(list(map(lambda x: x[0], coords)))
rightest = max(list(map(lambda x: x[0], coords)))
toppest = min(list(map(lambda x: x[1], coords)))
bottomest = max(list(map(lambda x: x[1], coords)))

cells_in_region = 0
for x in range(leftest, rightest+1):
  for y in range(toppest, bottomest+1):
    cell = (x, y)
    total_distance_to_cell = 0
    for coord in coords:
      total_distance_to_cell = total_distance_to_cell + distance_to_cell(coord, cell)
    if total_distance_to_cell < 10000:
      cells_in_region = cells_in_region + 1

print(cells_in_region)