position = 0
step_counter = 1
instructions = []

with open('input.txt') as file:
  for line in file:
    instructions.append(int(line.strip('\n')))

while True:
  # print("Step:", step_counter)
  # print("Starting at position:", position)
  # print("Instruction at position:", instructions[position])
  # print("All instructions:", instructions)
  new_position = position + instructions[position]
  if 0 <= new_position and new_position < len(instructions):
    # print("Changing instruction", position, "to:", instructions[position] + 1)
    instructions[position] = instructions[position] + 1
  else:
    print("\nFinished after", step_counter, "steps.")
    break
  position = new_position
  step_counter = step_counter + 1
  # print()

# print(step_counter)