depth = 11541
target_x = 14
target_y = 778

# depth = 510
# target_x = 10
# target_y = 10

grid = {}
for x in range(target_x+1):
  grid[x] = {}

def geologic_index(x, y):
  if x == 0 and y == 0:
    return 0
  if x == target_x and y == target_y:
    return 0
  if y == 0:
    return x * 16807
  if x == 0:
    return y * 48271

  # return erosion_level(x-1, y) * erosion_level(x, y-1)
  return ((grid[x-1][y] + depth) % 20183) * ((grid[x][y-1] + depth) % 20183)

def erosion_level(x, y):
  return (geologic_index(x, y) + depth) % 20183

def region_type(x, y):
  if erosion_level(x, y) % 3 == 0: return 'rocky'
  if erosion_level(x, y) % 3 == 1: return 'wet'
  if erosion_level(x, y) % 3 == 2: return 'narrow'

for x in range(target_x+1):
  for y in range(target_y+1):
    grid[x][y] = geologic_index(x, y)

total_risk = 0
for x in range(target_x+1):
  for y in range(target_y+1):
    total_risk = total_risk + ((grid[x][y] + depth) % 20183) % 3

# total_risk = 0
# for x in range(0, target_x+1):
#   for y in range(0, target_y+1):
#     total_risk = total_risk + (erosion_level(x, y) % 3)

print(total_risk)