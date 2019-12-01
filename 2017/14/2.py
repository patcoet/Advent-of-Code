from functools import reduce

def knot_hash(input):
  processed_input = list(map(ord, input)) + [17, 31, 73, 47, 23]
  lengths = processed_input

  numbers = [x for x in range(256)]

  current_position = 0
  skip_size = 0

  for i in range(64):
    for length in lengths:
      if length <= len(numbers):
        tmp = {}
        start = current_position
        end = current_position + length - 1

        for i in range(length):
          tmp[(end-i) % len(numbers)] = numbers[(start+i) % len(numbers)]

        for i in range(len(numbers)):
          if i in tmp.keys():
            numbers[i] = tmp[i]

        current_position = (current_position + length + skip_size) % len(numbers)
        skip_size = skip_size + 1

  blocks = []
  for i in range(16):
    tmp = []
    for n in range(len(numbers)):
      if n // 16 == i:
        tmp.append(numbers[n])
    blocks.append(tmp)

  dense_hash = [reduce(lambda x, y: x ^ y, block) for block in blocks]
  stringified_hash = ''.join(list(map(lambda x: format(x, '02x'), dense_hash)))
  binarified_hash = []
  for char in stringified_hash:
    binarified_hash.append(bin(int(char, 16)))
  return ''.join(map(lambda x: x[2:].zfill(4), binarified_hash))

input = 'ffayrhll'



def get_disk_grid(input):
  disk_grid = []
  for i in range(128):
    tmp = []
    for j in range(128):
      tmp.append(0)
    disk_grid.append(tmp)

  for i in range(128):
    string_to_hash = input + '-' + str(i)
    current_hash = knot_hash(string_to_hash)

    for j in range(len(current_hash)):
      disk_grid[i][j] = 1 * (current_hash[j] == '1')

  return disk_grid

# print(sum(map(sum, get_disk_grid(input))))

disk_grid = []
disk_grid = get_disk_grid(input)

# Look at each cell on the grid. If the cell or any of the cell's neighbors are in a region in the region list, add the cell and neighbors to that region. Otherwise, make a new region consisting of the cell and its neighbors, and add it to the region list.
region_list = []
for i in range(len(disk_grid)):
  row = disk_grid[i]
  for j in range(len(row)):
    if disk_grid[i][j] == 1:
      cell = (i, j)
      neighbors = []
      # if i > 0:
      #   neighbors.append((i-1, j))
      if i < len(disk_grid)-1:
        neighbors.append((i+1, j))
      # if j > 0:
      #   neighbors.append((i, j-1))
      if j < len(disk_grid)-1:
        neighbors.append((i, j+1))
      if cell == (127, 83):
        print(cell)
      should_make_new_region = True

      selected_region = set()
      for region in region_list:
        if cell in region:
          if cell == (127, 83):
            print("Cell already in region:", region)
          should_make_new_region = False
          selected_region = region
        for neighbor in neighbors:
          if neighbor in region:
            if cell == (127, 83):
              print("Neighbor already in region:", region)
            should_make_new_region = False
            selected_region = region

      selected_region.add(cell)
      for neighbor in neighbors:
        # print(neighbor)
        if disk_grid[neighbor[0]][neighbor[1]] == 1:
          selected_region.add(neighbor)

      if should_make_new_region:
        if cell == (127, 83):
          print("Decided to make new region:", selected_region)
        region_list.append(selected_region)


for i in range(128):
  for j in range(128):
    regions = []
    for k in range(len(region_list)):
      if (i, j) in region_list[k]:
        regions.append(region_list[k])
    thing = set()
    for region in regions:
      thing = thing.union(region)
      region_list.remove(region)
    if thing != set():
      region_list.append(thing)

print(region_list, len(region_list))
