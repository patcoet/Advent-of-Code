lines = []
with open('input.txt') as file:
  for line in file:
    lines.append(line.strip())

instructions = []
for line in lines:
  words = line.split(' ')
  must_be_finished = words[1]
  before_can_begin = words[-3]
  if not any([before_can_begin in instruction[0] for instruction in instructions]):
    instructions.append([before_can_begin, []])
  if not any([must_be_finished in instruction[0] for instruction in instructions]):
    instructions.append([must_be_finished, []])

for line in lines:
  words = line.split(' ')
  must_be_finished = words[1]
  before_can_begin = words[-3]
  for instruction in instructions:
    if before_can_begin == instruction[0]:
      instruction[1].append(must_be_finished)
      break

sorted_instructions = sorted(instructions)
order = []
while sorted_instructions != []:
  curr_instruction = None
  for instruction in sorted_instructions:
    if instruction[1] == []:
      curr_instruction = instruction
      break

  for instruction in sorted_instructions:
    if curr_instruction[0] in instruction[1]:
      instruction[1].remove(curr_instruction[0])

  order.append(curr_instruction[0])
  sorted_instructions.remove(curr_instruction)

print(''.join(order))
