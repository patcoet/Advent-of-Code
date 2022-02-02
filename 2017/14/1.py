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

  # return ''.join(list(map(lambda x: format(x, '02x'), dense_hash)))
  return list(map(bin, dense_hash))

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
    current_hash = ''.join(map(lambda x: x[2:], current_hash))
    for j in range(len(current_hash)):
      disk_grid[i][j] = 1 * (current_hash[j] == '1')

  return disk_grid

print(sum(map(sum, get_disk_grid(input))))
