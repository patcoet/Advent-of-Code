instructions = []
registers = [{}, {}]
with open('input.txt') as file:
  for line in file:
    words = line.strip().split(' ')
    instructions.append(words)

    for i in range(1, len(words)):
      for j in range(0, len(registers)):
        if words[i].isalpha() and words[i] not in registers[j].keys():
          registers[j][words[i]] = 0

registers[0]['queue'] = []
registers[1]['queue'] = []
registers[1]['p'] = 1
registers[0]['program_number'] = 0
registers[1]['program_number'] = 1
registers[0]['waiting'] = False
registers[1]['waiting'] = False

instruction_counter = [0, 0]
num_values_sent = [0, 0]

while True:
  for register in registers:
    instruction = instructions[instruction_counter[register['program_number']]]
    op = instruction[0]
    args = [instruction[i] for i in range(1, len(instruction))]

    if op == 'snd':
      value = register[args[0]] if args[0] in register.keys() else int(args[0])
      other_register_number = (register['program_number'] + 1) % len(registers)
      registers[other_register_number]['queue'].insert(0, value)
      num_values_sent[register['program_number']] += 1
    elif op == 'rcv':
      if register['queue'] == []:
        instruction_counter[register['program_number']] -= 1
        register['waiting'] = True
      else:
        register['waiting'] = False
        register[args[0]] = register['queue'].pop()
    else:
      arg1 = args[0]
      arg2 = register[args[1]] if args[1] in register.keys() else int(args[1])
      if op == 'set':
        register[arg1] = arg2
      elif op == 'add':
        register[arg1] = register[arg1] + arg2
      elif op == 'mul':
        register[arg1] = register[arg1] * arg2
      elif op == 'mod':
        register[arg1] = register[arg1] % arg2
      elif op == 'jgz':
        arg1 = int(register[arg1]) if arg1 in register.keys() else int(arg1)
        if arg1 > 0:
          instruction_counter[register['program_number']] += arg2 - 1
    instruction_counter[register['program_number']] += 1
  if instruction_counter[register['program_number']] < 0 or instruction_counter[register['program_number']] > len(instructions) or (registers[0]['waiting'] and registers[1]['waiting']):
    break

print(num_values_sent[1])
