lengths = [225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110]

numbers = [x for x in range(256)]

current_position = 0
skip_size = 0

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

print("First two numbers multiplied together:", numbers[0] * numbers[1])