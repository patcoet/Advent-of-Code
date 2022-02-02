# Day 5: Sunny with a Chance of Asteroids

memory = []

with open("input.txt") as file:
  memory = list(map(int, file.readline().strip().split(','))) # Turn puzzle input from "1,0,0" into [1,0,0].

def run(mem, inpt):
  ptr = 0 # The instruction pointer, which is the address of the current instruction.

  while (mem[ptr] != 99): # Read instructions and do stuff until coming across opcode 99.
    iop = str(mem[ptr])
    param_mode = iop[:-2][::-1]
    opcode = int(iop[-2:])

    modes = [0, 0, 0]
    for i in range(3):
      if len(param_mode) > i:
        modes[i] = int(param_mode[i])

    params = [0, 0, 0]
    for i in range(3):
      if len(mem) > ptr+i+1:
        if modes[i] == 0:
          params[i] = mem[ptr+i+1]
        else:
          params[i] = ptr+i+1

    if opcode == 1 or opcode == 2:
      params[2] = mem[ptr + 3]

      if opcode == 1:
        mem[params[2]] = mem[params[0]] + mem[params[1]]
      else:
        mem[params[2]] = mem[params[0]] * mem[params[1]]

      ptr += 4
    elif opcode == 3:
      params[0] = mem[ptr + 1]
      mem[params[0]] = inpt
      ptr += 2
    elif opcode == 4:
      if modes[0] == 0:
        params[0] = mem[ptr + 1]
      else:
        params[0] = ptr + 1

      print(mem[params[0]])

      ptr += 2
    elif opcode == 5:
      if mem[params[0]] != 0:
        ptr = mem[params[1]]
      else:
        ptr += 3
    elif opcode == 6:
      if mem[params[0]] == 0:
        ptr = mem[params[1]]
      else:
        ptr += 3
    elif opcode == 7:
      if mem[params[0]] < mem[params[1]]:
        mem[params[2]] = 1
      else:
        mem[params[2]] = 0
      ptr += 4
    elif opcode == 8:
      if mem[params[0]] == mem[params[1]]:
        mem[params[2]] = 1
      else:
        mem[params[2]] = 0
      ptr += 4

  return mem[0]

run(memory, 5)
