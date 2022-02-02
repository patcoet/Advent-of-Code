instructions = []
registers = {}
with open('input.txt') as file:
  for line in file:
    words = line.strip().split(' ')
    instructions.append(words)

    for i in range(1, len(words)):
      if words[i].isalpha() and words[i] not in registers.keys():
        registers[words[i]] = 0

last_frequency_played = None
i = 0
while 0 <= i and i < len(instructions):
  instruction = instructions[i]
  # print(i, instruction, registers)
  op = instruction[0]
  args = [instruction[i] for i in range(1, len(instruction))]
  if op == 'snd':
    value = registers[args[0]] if args[0] in registers.keys() else int(args[0])
    last_frequency_played = value
  elif op == 'rcv':
    value = registers[args[0]] if args[0] in registers.keys() else int(args[0])
    if value != 0:
      print("rcv")
      break
  else:
    arg1 = args[0]
    arg2 = registers[args[1]] if args[1] in registers.keys() else int(args[1])
    if op == 'set':
      registers[arg1] = arg2
    elif op == 'add':
      registers[arg1] = registers[arg1] + arg2
    elif op == 'mul':
      registers[arg1] = registers[arg1] * arg2
    elif op == 'mod':
      registers[arg1] = registers[arg1] % arg2
    elif op == 'jgz':
      if registers[arg1] > 0:
        i = i + arg2 - 1
  i = i + 1

print(last_frequency_played)
