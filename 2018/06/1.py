from collections import Counter

coords = []
with open('input.txt') as file:
  for line in file:
    xy = line.strip().split(',')
    coords.append((int(xy[0]), int(xy[1])))

def closest_coord(cell):
  (x1, y1) = cell
  distances = []
  for coord in coords:
    (x2, y2) = coord
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    manhattan_distance = dx + dy
    distances.append([manhattan_distance, (coord)])
  return list(filter(lambda d: d[0] == min(distances)[0], distances))

def coord_area_is_finite(coord):
  (x0, y0) = coord

  leftest = min(list(map(lambda x: x[0], coords)))
  rightest = max(list(map(lambda x: x[0], coords)))
  toppest = min(list(map(lambda x: x[1], coords)))
  bottomest = max(list(map(lambda x: x[1], coords)))

  left_quad_has_other_coord = False
  top_quad_has_other_coord = False
  right_quad_has_other_coord = False
  bottom_quad_has_other_coord = False

  d_leftest = x0 - leftest
  for i in range(1, d_leftest+1):
    for j in range(-i, i+1):
      if (x0-i, y0+j) in coords:
        left_quad_has_other_coord = True

  d_toppest = y0 - toppest
  for i in range(1, d_toppest+1):
    for j in range(-i, i+1):
      if (x0+j, y0-i) in coords:
        top_quad_has_other_coord = True

  d_rightest = rightest - x0
  for i in range(1, d_rightest+1):
    for j in range(-i, i+1):
      if (x0+i, y0+j) in coords:
        right_quad_has_other_coord = True

  d_bottomest = bottomest - y0
  for i in range(1, d_bottomest+1):
    for j in range(-i, i+1):
      if (x0+j, y0+i) in coords:
        bottom_quad_has_other_coord = True

  return all([left_quad_has_other_coord, top_quad_has_other_coord, right_quad_has_other_coord, bottom_quad_has_other_coord])


leftest = min(list(map(lambda x: x[0], coords)))
rightest = max(list(map(lambda x: x[0], coords)))
toppest = min(list(map(lambda x: x[1], coords)))
bottomest = max(list(map(lambda x: x[1], coords)))

cells_closest_to_just_one_coord = map(lambda x: x[0][1], filter(lambda x: len(x) == 1, [closest_coord((x,y)) for y in range(toppest, bottomest+1) for x in range(leftest, rightest+1)]))
unfiltered_areas = Counter(cells_closest_to_just_one_coord).most_common()
# print("Unfiltered areas:", unfiltered_areas)
filtered_areas = list(filter(lambda x: coord_area_is_finite(x[0]), unfiltered_areas))
# print("Filtered areas:", filtered_areas)
print("Biggest area:", filtered_areas[0])