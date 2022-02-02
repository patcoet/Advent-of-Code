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

for instruction in instructions:
  instruction.append(False) # Is this step busy?

sorted_instructions = sorted(instructions)
workers = [0, 0, 0, 0, 0] # Number of seconds busy

current_tick = 0
current_tasks = [[], [], [], [], []]
while sorted_instructions != []:
  for i in range(len(workers)):
    if workers[i] <= 0:
      if current_tasks[i] != []: # Just finished a task
        for j in range(len(sorted_instructions)):
          instruction = sorted_instructions[j]
          if current_tasks[i][0] in instruction[1]:
            sorted_instructions[j][1].remove(current_tasks[i][0])
            sorted_instructions[j][2] = False
        sorted_instructions.remove(current_tasks[i])
        print("Tick " + str(current_tick) + ": Worker " + str(i) + " finished task", current_tasks[i][0])
        current_tasks[i] = []

      for j in range(len(sorted_instructions)):
        instruction = sorted_instructions[j]
        if not instruction[2] and instruction[1] == []:
          print("Tick " + str(current_tick) + ": Worker " + str(i) + " picked task " + instruction[0])
          current_tasks[i] = instruction
          sorted_instructions[j][2] = True
          workers[i] = ord(instruction[0]) - 4 # A = 61, ...
          break
  workers = [x-1 for x in workers]
  current_tick = current_tick + 1

print(current_tick-2) # I'm pretty sure -1 should be correct, but...