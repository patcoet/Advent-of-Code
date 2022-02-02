inputt = 'input.txt'
lines = []
with open(inputt) as file:
  for line in file:
    lines.append(line.strip('\n'))

starting_state = lines[0][-2]
total_steps = int(lines[1].split(' ')[-2])

blocks = []
start = 0
end = 0
for i in range(len(lines)):
  if lines[i] == "":
    start = i
    end = start + 10
    blocks.append(lines[start+1 : end+1])

for i in range(len(blocks)):
  blocks[i] = blocks[i][0:9]

for block in blocks:
  for i in range(len(block)):
    block[i] = block[i].strip()

instructions = {}

for block in blocks:
  if_state = block[0][-2]
  instructions[if_state] = {}

  instructions[if_state]['write_if_zero'] = int(block[2][-2])
  instructions[if_state]['move_if_zero'] = block[3].split(' ')[-1].strip('.')
  instructions[if_state]['state_if_zero'] = block[4][-2]

  instructions[if_state]['write_if_one'] = int(block[6][-2])
  instructions[if_state]['move_if_one'] = block[7].split(' ')[-1].strip('.')
  instructions[if_state]['state_if_one'] = block[8][-2]

def tape_value(tape, position):
  if (not position in tape) or tape[position] == 0:
    return 0
  else:
    return 1

steps_taken = 0
current_state = starting_state
current_position = 0

tape = {}

min_tape_position = 0
max_tape_position = 0

# print(instructions)

while steps_taken < total_steps:
  current_value = tape_value(tape, current_position)
  direction = None
  new_state = None
  to_write = None

  if current_value == 0:
    direction = instructions[current_state]['move_if_zero']
    new_state = instructions[current_state]['state_if_zero']
    to_write = instructions[current_state]['write_if_zero']
  else:
    direction = instructions[current_state]['move_if_one']
    new_state = instructions[current_state]['state_if_one']
    to_write = instructions[current_state]['write_if_one']

  # print("Current position, state, value:", current_position, current_state, current_value)
  # print("Going in direction:", direction)

  tape[current_position] = to_write
  current_state = new_state

  if direction == 'left':
    current_position = current_position - 1
  else:
    current_position = current_position + 1

  steps_taken = steps_taken + 1
  min_tape_position = min(min_tape_position, current_position)
  max_tape_position = max(max_tape_position, current_position)

# print(tape)

checksum = 0
for i in range(min_tape_position, max_tape_position+1):
  checksum = checksum + tape_value(tape, i)

print(checksum)