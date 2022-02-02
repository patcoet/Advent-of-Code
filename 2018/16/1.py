import re

lines = ""

with open('input.txt') as file:
  lines = file.read()

p = re.compile('Before: \[(\d), (\d), (\d), (\d)\]\n(\d*) (\d) (\d) (\d)\nAfter:  \[(\d), (\d), (\d), (\d)\]')

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

ops = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

num_samples_like_three_or_more = 0
for thing in p.finditer(lines):
  before = [int(x) for x in [thing[1], thing[2], thing[3], thing[4]]]
  opcode = int(thing[5])
  input1 = int(thing[6])
  input2 = int(thing[7])
  output = int(thing[8])
  after = [int(x) for x in [thing[9], thing[10], thing[11], thing[12]]]

  num_similar_opcodes = 0
  for operation in ops:
    if op(before, operation, input1, input2, output) == after:
      num_similar_opcodes = num_similar_opcodes + 1
  if num_similar_opcodes >= 3:
    num_samples_like_three_or_more = num_samples_like_three_or_more + 1

print(num_samples_like_three_or_more)
