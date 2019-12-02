# Day 2: 1202 Program Alarm
memory = [] # Variable names changed from part 1 to agree with part 2 terminology.

with open("input.txt") as file:
  memory = list(map(int, file.readline().strip().split(','))) # Turn puzzle input from "1,0,0" into [1,0,0].

def run(mem, input1, input2): # Take a program and two inputs and return the value left at position 0.
  ptr = 0 # The instruction pointer, which is the address of the current instruction.
  mem[1] = input1
  mem[2] = input2

  while (mem[ptr] != 99): # Read instructions and do stuff until coming across opcode 99.
    opcode = mem[ptr]
    prm1 = mem[ptr + 1]
    prm2 = mem[ptr + 2]
    prm3 = mem[ptr + 3]

    if opcode == 1:
      mem[prm3] = mem[prm1] + mem[prm2]
    elif opcode == 2:
      mem[prm3] = mem[prm1] * mem[prm2]

    ptr += 4

  return mem[0]

target_output = 19690720

# Try running the program with inputs from 0 and 0 to 99 and 99 until we find the input combination that produces our target output:
for noun, verb, output in [(noun, verb, run(memory.copy(), noun, verb)) for noun in range(100) for verb in range(100)]:
  if output == target_output:
    print(f"noun = {noun}; verb = {verb}; 100 * noun + verb = {100 * noun + verb}")
    break
