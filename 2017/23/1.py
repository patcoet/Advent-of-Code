def read(filename):
  instructions = []
  with open(filename) as file:
    for line in file:
      instructions.append(line.strip().split(' '))
  return instructions

def process_instructions(instructions, registers):
  mul_counter = 0
  i = 0

  while 0 <= i < len(instructions):
    instr = instructions[i]
    op = instr[0]
    arg1 = instr[1]
    arg2 = int(registers[instr[2]]) if instr[2] in registers.keys() else int(instr[2])

    if op == 'set':
      registers[arg1] = arg2
    elif op == 'sub':
      registers[arg1] = registers[arg1] - arg2
    elif op == 'mul':
      mul_counter = mul_counter + 1
      registers[arg1] = registers[arg1] * arg2
    else: # jnz
      if arg1 in registers.keys():
        arg1 = int(registers[arg1])
      else:
        arg1 = int(arg1)
      if arg1 != 0:
        i = i + arg2 - 1
    i = i + 1

  return mul_counter

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
print(process_instructions(read('input.txt'), registers))
