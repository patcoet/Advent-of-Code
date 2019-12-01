pointer_register = None
instructions = []

with open('input.txt') as file:
  for line in file:
    if "#ip" in line:
      pointer_register = int(line[-2])
    else:
      words = line.strip().split(' ')
      instructions.append([words[0], int(words[1]), int(words[2]), int(words[3])])

def op(registers, operation, a, b, c):
  if operation == 'addr':
    return registers[:c] + [registers[a] + registers[b]] + registers[c+1:]
  if operation == 'addi':
    return registers[:c] + [registers[a] + b] + registers[c+1:]

  if operation == 'mulr':
    return registers[:c] + [registers[a] * registers[b]] + registers[c+1:]
  if operation == 'muli':
    return registers[:c] + [registers[a] * b] + registers[c+1:]

  if operation == 'banr':
    return registers[:c] + [registers[a] & registers[b]] + registers[c+1:]
  if operation == 'bani':
    return registers[:c] + [registers[a] & b] + registers[c+1:]

  if operation == 'borr':
    return registers[:c] + [registers[a] | registers[b]] + registers[c+1:]
  if operation == 'bori':
    return registers[:c] + [registers[a] | b] + registers[c+1:]

  if operation == 'setr':
    return registers[:c] + [registers[a]] + registers[c+1:]
  if operation == 'seti':
    return registers[:c] + [a] + registers[c+1:]

  if operation == 'gtir':
    return registers[:c] + [1 if a > registers[b] else 0] + registers[c+1:]
  if operation == 'gtri':
    return registers[:c] + [1 if registers[a] > b else 0] + registers[c+1:]
  if operation == 'gtrr':
    return registers[:c] + [1 if registers[a] > registers[b] else 0] + registers[c+1:]

  if operation == 'eqir':
    return registers[:c] + [1 if a == registers[b] else 0] + registers[c+1:]
  if operation == 'eqri':
    return registers[:c] + [1 if registers[a] == b else 0] + registers[c+1:]
  if operation == 'eqrr':
    return registers[:c] + [1 if registers[a] == registers[b] else 0] + registers[c+1:]

def go_until_pattern(registers, pointer_register):
  while 0 <= registers[pointer_register] and registers[pointer_register] < len(instructions):
    curr_instruction = instructions[registers[pointer_register]]
    if registers[pointer_register] == 28:
      return registers[5]
    registers = op(registers, curr_instruction[0], curr_instruction[1], curr_instruction[2], curr_instruction[3])

    registers[pointer_register] = registers[pointer_register] + 1

print(go_until_pattern([0, 0, 0, 0, 0, 0], pointer_register))

# Every time instruction 28 is executed, r5 is compared to r0. If they're equal, execution stops two (or whatever) steps later.
# If r0 starts at the first value r5 is at the first time it reaches 28, execution stops as quickly as possible.