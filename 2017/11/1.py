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

# Look through the path. If we see a step ne, check if we've previously taken
# a step s. If yes, replace ne with se and s with nothing. Etc. Then count how
# many steps are still int he path.
# That's a lot to write out, though. Can we like assign each direction an int
# and add them together and something something?
# nw is (-1, 1), n is (0, 1), ne is (1, 1), sw is (-1, -1), s is (0, -1), ...
# Then n+s = (0, 0) and ne+sw = (0, 0), but nw+s = (-1, 0) and nw+ne = (0, 2).
# If we say n = (0, 2) and s = (0, -2) everything is fine except those.
# Or maybe that's actually correct?

end_coord = reduce(lambda x, y: (x[0]+y[0], x[1]+y[1]), path)

# print(end_coord)

# Go sideways until the right x coord, then up or down until the end

(end_x, end_y) = end_coord
curr_coord = (0, 0)
steps_needed = 0
while curr_coord[0] != end_coord[0]:
  (curr_x, curr_y) = curr_coord
  move_x = 0
  move_y = 0
  if curr_x < end_x:
    move_x = 1
  else:
    move_x = -1
  if curr_y < end_y:
    move_y = 1
  else:
    move_y = -1

  curr_coord = (curr_x + move_x, curr_y + move_y)
  steps_needed = steps_needed + 1

# print(curr_coord)

while curr_coord != end_coord:
  (curr_x, curr_y) = curr_coord
  move_y = 0
  if curr_y < end_y:
    move_y = 2
  else:
    move_y = -2

  curr_coord = (curr_x, curr_y + move_y)
  steps_needed = steps_needed + 1

# print(curr_coord)
print("Steps needed:", steps_needed)
