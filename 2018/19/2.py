import math
from collections import Counter

registers = [1, 0, 0, 0, 0, 0]
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

seen_instructions = Counter()
while 0 <= registers[pointer_register] and registers[pointer_register] < len(instructions):
  curr_instruction = instructions[registers[pointer_register]]
  if seen_instructions[registers[pointer_register]] > 1:
    break
  registers = op(registers, curr_instruction[0], curr_instruction[1], curr_instruction[2], curr_instruction[3])

  registers[pointer_register] = registers[pointer_register] + 1
  seen_instructions[registers[pointer_register]] += 1

big_num = max(registers)
print(big_num)
divisors = [n for n in range(1, int(math.sqrt(big_num))+1) if big_num % n == 0]
result = sum(divisors + [big_num // n for n in divisors])

print(result)

