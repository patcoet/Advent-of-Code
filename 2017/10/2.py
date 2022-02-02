from functools import reduce

inputt = "225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110"
# inputt = "AoC 2017"
processed_input = list(map(ord, inputt)) + [17, 31, 73, 47, 23]
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

print(''.join(list(map(lambda x: format(x, '02x'), dense_hash))))

