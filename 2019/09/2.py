# Day 9: Sensor Boost
# Extend Intcode computer functionality for (supposedly) the last time, with mode 2 and arbitrary memory.

def run(mem, inpt):
  mem += [0] * 200 # I think ideally we'd add an infinite list of 0s and access mem lazily instead (or make mem a map instead of a list and have a function for accessing it that adds a 0 if an address doesn't exist, or something), but this works and I'm lazy.
  ptr = 0
  rel = 0 # The relative base, used in mode 2.
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
          params[i] = mem[ptr + (i + 1)]
        elif modes[i] == "1":
          params[i] = ptr + (i + 1)
        elif modes[i] == "2":
          params[i] = mem[ptr + (i + 1)] + rel

    ptr += num_params + 1


    if opcode == 1:   # p3 = p1 + p2
      mem[params[2]] = mem[params[0]] + mem[params[1]]

    elif opcode == 2: # p3 = p1 * p2
      mem[params[2]] = mem[params[0]] * mem[params[1]]

    elif opcode == 3: # input to p1
      mem[params[0]] = inpt

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

  return output

memory = []

with open("input.txt") as file:
  memory = list(map(int, file.readline().strip().split(',')))

print(f"Program output: {run(memory, 2)}")
