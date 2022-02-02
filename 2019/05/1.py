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

    if opcode == 1 or opcode == 2:
      if modes[0] == 0:
        prm1 = mem[ptr + 1]
      else:
        prm1 = ptr + 1

      if modes[1] == 0:
        prm2 = mem[ptr + 2]
      else:
        prm2 = ptr + 2

      prm3 = mem[ptr + 3]

      if opcode == 1:
        mem[prm3] = mem[prm1] + mem[prm2]
      else:
        mem[prm3] = mem[prm1] * mem[prm2]

      ptr += 4
    elif opcode == 3:
      prm1 = mem[ptr + 1]
      mem[prm1] = inpt
      ptr += 2
    elif opcode == 4:
      if modes[0] == 0:
        prm1 = mem[ptr + 1]
      else:
        prm1 = ptr + 1

      print(mem[prm1])

      ptr += 2

  return mem[0]

run(memory, 1)
