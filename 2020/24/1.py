instructions = []

with open("input.txt") as file:
  for line in file:
    i = 0
    instruction = []
    while i < len(line.strip()):
      c1 = line[i]
      c2 = line[i:i+2]

      if c1 == "e":
        n = (2, 0)
      elif c2 == "se":
        n = (1, 1)
      elif c2 == "sw":
        n = (-1, 1)
      elif c1 == "w":
        n = (-2, 0)
      elif c2 == "nw":
        n = (-1, -1)
      else:
        n = (1, -1)

      instruction.append(n)

      if line[i] == "e" or line[i] == "w":
        i += 1
      else:
        i += 2
    instructions.append(instruction)

end_coords = {}

for instruction in instructions:
  coord = (0, 0)
  for step in instruction:
    x0, y0 = coord
    x, y = step
    coord = (x0+x, y0+y)
  if coord not in end_coords.keys():
    end_coords[coord] = 1
  else:
    end_coords[coord] += 1


print(len([x for x in end_coords.values() if x % 2 == 1]))
