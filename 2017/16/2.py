spin_or_exchange_steps = []
partner_steps = []
with open('input.txt') as file:
  steps = file.read().strip().split(',')
  for step in steps:
    instruction = step[0]
    if instruction == 's':
      spin_or_exchange_steps.append([instruction, int(step[1:])])
    else:
      parameter1 = step[1:].split('/')[0]
      parameter2 = step[1:].split('/')[1]
      if instruction == 'x':
        spin_or_exchange_steps.append([instruction, int(parameter1), int(parameter2)])
      elif instruction == 'p':
        partner_steps.append([instruction, parameter1, parameter2]
          )


periodicity_a = None
line = [chr(x) for x in range(ord('a'), ord('p')+1)]
seen_lines = []
for i in range(100):
  if ''.join(line) in seen_lines:
    periodicity_a = len(seen_lines)
    break
  else:
    seen_lines.append(''.join(line))
    for step in spin_or_exchange_steps:
      instruction = step[0]
      if instruction == 's':
        num = step[1]
        line = line[-num:] + line[:-num]
      elif instruction == 'x':
        a = step[1]
        b = step[2]
        tmp = line[a]
        line[a] = line[b]
        line[b] = tmp

periodicity_b = None
line = [chr(x) for x in range(ord('a'), ord('p')+1)]
seen_lines = []
for i in range(100):
  if ''.join(line) in seen_lines:
    periodicity_b = len(seen_lines)
    break
  else:
    seen_lines.append(''.join(line))
    for step in partner_steps:
      instruction = step[0]
      a = step[1]
      b = step[2]
      line = list(''.join(line).replace(a, 'x').replace(b, a).replace('x', b))


num_dances = 1000000000
line = [chr(x) for x in range(ord('a'), ord('p')+1)]

for i in range(num_dances % periodicity_a):
  for step in spin_or_exchange_steps:
    instruction = step[0]
    if instruction == 's':
      num = step[1]
      line = line[-num:] + line[:-num]
    elif instruction == 'x':
      a = step[1]
      b = step[2]
      tmp = line[a]
      line[a] = line[b]
      line[b] = tmp
for i in range(num_dances % periodicity_b):
  for step in partner_steps:
    instruction = step[0]
    a = step[1]
    b = step[2]
    line = list(''.join(line).replace(a, 'x').replace(b, a).replace('x', b))

print(''.join(line))
