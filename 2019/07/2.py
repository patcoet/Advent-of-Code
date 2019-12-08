# Day 7: Amplification Circuit

def run(memory, inpt):
  mems = [memory.copy(), memory.copy(), memory.copy(), memory.copy(), memory.copy()] # `[memory.copy()] * 5` makes 5 of the same copy, and I don't want to go through the trouble of looking up another convenient way to do this.
  inputs = [[inpt[0], 0], [inpt[1]], [inpt[2]], [inpt[3]], [inpt[4]]] # We need to keep track of memory
  ptrs = [0, 0, 0, 0, 0]                                              # and pointer states for this.
  i = 0 # Index of currently running amplifier.
  while mems[4][ptrs[4]] != 99: # Keep running until amplifier E has finished.
    mem = mems[i]
    while True:
      ptr = ptrs[i]

      instr = str(mem[ptr])
      modes = instr[:-2][::-1].ljust(2, "0") # Pad to make implicit 0s explicit.
      opcode = int(instr[-2:])

      if opcode == 99: break


      p1 = mem[ptr + 1]
      if opcode != 3 and modes[0] == "0": # If in position mode,
        p1 = mem[p1]                      # the first parameter is an address.
      if opcode not in [3, 4]:
        p2 = mem[ptr + 2]
        if modes[1] == "0":
          p2 = mem[p2]
      if opcode in [1, 2, 7, 8]:
        p3 = mem[ptr + 3]


      if opcode == 1:   # p3 = p1 + p2
        mem[p3] = p1 + p2
        ptrs[i] += 4

      elif opcode == 2: # p3 = p1 * p2
        mem[p3] = p1 * p2
        ptrs[i] += 4

      elif opcode == 3: # input to p1
        if len(inputs[i]) == 0: # If there's no input waiting for this amplifier,
          break                 # pause execution. (Memory and pointer states are saved in mems and ptrs.)
        else:
          mem[p1] = inputs[i].pop(0)
        ptrs[i] += 2

      elif opcode == 4: # output p1
        inputs[(i+1) % len(inputs)].append(p1) # Set the next amplifier's input to this output.
        ptrs[i] += 2

      elif opcode == 5: # jump to p2 if p1 != 0
        if p1 != 0:
          ptrs[i] = p2
        else:
          ptrs[i] += 3

      elif opcode == 6: # jump to p2 if p1 == 0
        if p1 == 0:
          ptrs[i] = p2
        else:
          ptrs[i] += 3

      elif opcode == 7: # p1 < p2
        mem[p3] = 1 * (p1 < p2)
        ptrs[i] += 4

      elif opcode == 8: # p1 == p2
        mem[p3] = 1 * (p1 == p2)
        ptrs[i] += 4

    i = (i + 1) % len(mems) # When we've run the program for amplifier E, go back to A.

  return inputs[0][0] # Amplifier A's last input value, which is amplifier E's last output value.

memory = []

with open("input.txt") as file:
  memory = list(map(int, file.readline().strip().split(',')))

import itertools

signals = [(run(memory.copy(), sequence), sequence) for sequence in itertools.permutations(range(5,10))]
max_signal, max_sequence = max(signals)

print(f"Highest signal is {max_signal}, from setting {max_sequence}.")
