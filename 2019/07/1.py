def run(mem, inpt):
  ptr = 0
  output = []

  while mem[ptr] != 99:
    instr = str(mem[ptr])
    modes = instr[:-2][::-1].ljust(2, "0")
    opcode = int(instr[-2:])

    v1 = mem[ptr + 1]
    if opcode != 3 and modes[0] == "0":
      v1 = mem[v1]

    if opcode not in [3, 4]:
      v2 = mem[ptr + 2]
      if modes[1] == "0":
        v2 = mem[v2]

    if opcode in [1, 2, 7, 8]:
      v3 = mem[ptr + 3]

    if opcode == 1:
      mem[v3] = v1 + v2
      ptr += 4
    elif opcode == 2:
      mem[v3] = v1 * v2
      ptr += 4
    elif opcode == 3:
      mem[v1] = inpt.pop(0)
      ptr += 2
    elif opcode == 4:
      output.append(v1)
      ptr += 2
    elif (opcode == 5 and v1 != 0) or (opcode == 6 and v1 == 0):
      ptr = v2
    elif opcode == 5 or opcode == 6:
      ptr += 3
    elif (opcode == 7 and v1 < v2) or (opcode == 8 and v1 == v2):
      mem[v3] = 1
      ptr += 4
    elif opcode == 7 or opcode == 8:
      mem[v3] = 0
      ptr += 4

  if len(output) == 1:
    return output[0]
  else:
    return output

def reprun(mem, sequence):
  prev = 0
  for setting in sequence:
    prev = run(mem, [setting, prev])
  return prev

memory = []

with open("input.txt") as file:
  memory = list(map(int, file.readline().strip().split(',')))

import itertools

signals = [reprun(memory, sequence) for sequence in itertools.permutations(range(5))]

print(f"Highest signal that can be sent: {max(signals)}")
