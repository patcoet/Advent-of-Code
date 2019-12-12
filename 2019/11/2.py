# Day 11: Space Police (Part 2)
# Read what was painted.

def run(mem, ptr, rel, inpt):
  output = []

  while ptr != 99:
    instr = str(mem[ptr])
    modes = instr[:-2][::-1].ljust(3, "0") # Pad to make implicit 0s explicit.
    opcode = int(instr[-2:])

    if opcode == 99: break

    num_params = 1
    if opcode in [1, 2, 7, 8]:
      num_params = 3
    elif opcode in [5, 6]:
      num_params = 2

    params = [None, None, None]
    for i in range(3):
      if num_params >= (i + 1):
        if modes[i] == "0":
          if mem[ptr + (i + 1)] not in mem.keys():
            mem[mem[ptr + (i + 1)]] = 0
          params[i] = mem[ptr + (i + 1)]
        elif modes[i] == "1":
          if ptr + (i + 1) not in mem.keys():
            mem[ptr + (i + 1)] = 0
          params[i] = ptr + (i + 1)
        elif modes[i] == "2":
          if mem[ptr + (i + 1)] + rel not in mem.keys():
            mem[mem[ptr + (i + 1)] + rel] = 0
          params[i] = mem[ptr + (i + 1)] + rel

    ptr += num_params + 1

    if opcode == 1:   # p3 = p1 + p2
      mem[params[2]] = mem[params[0]] + mem[params[1]]

    elif opcode == 2: # p3 = p1 * p2
      mem[params[2]] = mem[params[0]] * mem[params[1]]

    elif opcode == 3: # input to p1
      if inpt == []:
        ptr -= num_params + 1
        break
      else:
        mem[params[0]] = inpt.pop()

    elif opcode == 4: # output p1
      output.append(mem[params[0]])

    elif opcode == 5: # jump to p2 if p1 != 0
      if mem[params[0]] != 0:
        ptr = mem[params[1]]

    elif opcode == 6: # jump to p2 if p1 == 0
      if mem[params[0]] == 0:
        ptr = mem[params[1]]

    elif opcode == 7: # p1 < p2
      mem[params[2]] = 1 * (mem[params[0]] < mem[params[1]])

    elif opcode == 8: # p1 == p2
      mem[params[2]] = 1 * (mem[params[0]] == mem[params[1]])

    elif opcode == 9: # rel += p1
      rel += mem[params[0]]

  return mem, ptr, rel, output

memory = {}

with open("input.txt") as file:
  mem = list(map(int, file.readline().strip().split(',')))
for i, v in enumerate(mem):
  memory[i] = v

def pprint(paint, position, direction):
  w = 50
  h = 10
  for y in range(-h, h):
    s = ""
    for x in range(-w, w):
      if (x, y) == position:
        if direction == 0:
          s += "^"
        elif direction == 1:
          s += ">"
        elif direction == 2:
          s += "v"
        elif direction == 3:
          s += "<"
      elif (x, y) in paint.keys() and paint[(x, y)] == 1:
        s += "#"
      else:
        s += " "
    print(s)
  print()


position = (0, 0)
direction = 0 # 0 for up, 1 for right, 2 for down, and 3 for left.
paint = {}
ptr = 0
rel = 0
inpt = [1]
done = False

while not done:
  memory, ptr, rel, output = run(memory, ptr, rel, inpt)

  color = output[0]
  new_dir = output[1]

  if color == 0:
    paint[position] = 0
  elif color == 1:
    paint[position] = 1

  if new_dir == 0:
    direction = (direction - 1) % 4
  elif new_dir == 1:
    direction = (direction + 1) % 4

  x, y = position
  if direction == 0:
    y -= 1
  elif direction == 1:
    x += 1
  elif direction == 2:
    y += 1
  elif direction == 3:
    x -= 1
  position = (x, y)

  inpt = [0]
  if position in paint.keys() and paint[position] == 1:
    inpt = [1]

  if memory[ptr] == 99:
    done = True

pprint(paint, position, direction)
# print(len(paint))