def read(filename):
  instructions = []
  with open(filename) as file:
    for line in file:
      instructions.append(line.strip().split(' '))
  return instructions

# def process_instructions(instructions, registers):
#   mul_counter = 0
#   i = 0

#   while 0 <= i < len(instructions):
#     instr = instructions[i]
#     op = instr[0]
#     arg1 = instr[1]
#     arg2 = int(registers[instr[2]]) if instr[2] in registers.keys() else int(instr[2])

#     if op == 'set':
#       registers[arg1] = arg2
#     elif op == 'sub':
#       registers[arg1] = registers[arg1] - arg2
#     elif op == 'mul':
#       mul_counter = mul_counter + 1
#       registers[arg1] = registers[arg1] * arg2
#     else: # jnz
#       if arg1 in registers.keys():
#         arg1 = int(registers[arg1])
#       else:
#         arg1 = int(arg1)
#       if arg1 != 0:
#         i = i + arg2 - 1
#     i = i + 1
#     print(registers)

#   return mul_counter

# registers = {'a': 1, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0}
# print(process_instructions(read('input.txt'), registers))


# set b 79         b = 79
# set c b          c = b (= 79)
# jnz a 2          if a == 0:
# jnz 1 5            goto label1
# mul b 100        b *= 100 (= 7900)
# sub b -100000    b += 100000 (= 107900)
# set c b          c = b (= 107900)
# sub c -17000     c = b + 17000 (= 124900)

# So, with a starting at 1, the registers after this setup will be:
# [1, 107900, 124900, 0, 0, 0, 0, 0]
# And then the following is run until halt:
# set f 1          label1: f = 1
# set d 2          d = 2
# set e 2          label2: e = 2
# set g d          label3: g = d
# mul g e          g *= e
# sub g b          g -= b
# jnz g 2          if g == 0 (g == b) (d*e == b):
# set f 0            f = 0
# sub e -1         e += 1
# set g e          g = e
# sub g b          g -= b
# jnz g -8         if g != 0 (e != b): goto label3
# sub d -1         d += 1
# set g d          g = d
# sub g b          g -= b
# jnz g -13        if g != 0 (d != b): goto label2
# jnz f 2          if f == 0:
# sub h -1           h += 1
# set g b          g = b
# sub g c          g = b - c
# jnz g 2          if b == c:
# jnz 1 3            halt
# sub b -17        else: b += 17
# jnz 1 -23              goto label1

# So, f gets set to 0 if g*e = b, where b = 107900, 107917, ..., 124900.
# If f == 0, h is incremented.
# So, h is incremented whenever b is not prime, and the total number is the number of non-primes between b and c?

import math
counter = 0
for x in range(107900, 124901, 17):
  if any(x % i == 0 for i in range(2, int(math.sqrt(x)))):
    counter = counter + 1

print(counter)
