# Day 2: 1202 Program Alarm
program = []

with open("input.txt") as file:
  program = list(map(int, file.readline().strip().split(','))) # Turn puzzle input from "1,0,0" into [1,0,0].

# Puzzle instructions say to do this:
program[1] = 12
program[2] = 2

for i, num in enumerate(program):
  if i % 4 == 0: # We're reading an opcode, doing stuff, then stepping forward 4 positions.
    opcode = num

    if opcode == 99: # This is here rather than down with the other ifs to prevent array bounds errors.
      break          # (Because otherwise, for the example of [1,9,10,3,2,3,11,0,99,30,40,50], we would at the end be doing pos1 = program[30], etc.)

    pos1 = program[i+1]
    pos2 = program[i+2]
    pos3 = program[i+3]

    if opcode == 1:
      program[pos3] = program[pos1] + program[pos2]
    elif opcode == 2:
      program[pos3] = program[pos1] * program[pos2]

print(f"Value at position 0: {program[0]}")
