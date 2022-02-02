from functools import reduce

inputt = 'input.txt'
path = []

with open(inputt) as file:
  path = file.read().strip().split(',')

for i in range(len(path)):
  d = path[i]
  if d == 'n':
    path[i] = (0, 2)
  elif d == 'ne':
    path[i] = (1, 1)
  elif d == 'se':
    path[i] = (1, -1)
  elif d == 's':
    path[i] = (0, -2)
  elif d == 'sw':
    path[i] = (-1, -1)
  elif d == 'nw':
    path[i] = (-1, 1)

end_coord = reduce(lambda x, y: (x[0]+y[0], x[1]+y[1]), path)

# (end_x, end_y) = end_coord
# curr_coord = (0, 0)
def steps_needed_to_coord(target_coord):
  (target_x, target_y) = target_coord
  curr_coord = (0, 0)
  steps_needed = 0

  while curr_coord[0] != target_coord[0]:
    (curr_x, curr_y) = curr_coord
    move_x = 0
    move_y = 0
    if curr_x < target_x:
      move_x = 1
    else:
      move_x = -1
    if curr_y < target_y:
      move_y = 1
    else:
      move_y = -1

    curr_coord = (curr_x + move_x, curr_y + move_y)
    steps_needed = steps_needed + 1

  while curr_coord != target_coord:
    (curr_x, curr_y) = curr_coord
    move_y = 0
    if curr_y < target_y:
      move_y = 2
    else:
      move_y = -2

    curr_coord = (curr_x, curr_y + move_y)
    steps_needed = steps_needed + 1

  return steps_needed

print("Steps needed:", steps_needed_to_coord(end_coord))

max_distance = 0
for i in range(len(path)):
  path_so_far = path[0:i+1]
  tmp_end_coord = reduce(lambda x, y: (x[0]+y[0], x[1]+y[1]), path_so_far)
  curr_distance = steps_needed_to_coord(tmp_end_coord)
  max_distance = max(max_distance, curr_distance)
  # print(tmp_end_coord)
  # if i > 3: break

print("Furthest distance reached:", max_distance)