instructions = []

with open("input.txt") as file:
  for line in file:
    instructions.append([line.strip()[0], int(line.strip()[1:])])

facing = 0 # 0 east, 90 south
x = 0
y = 0

for instruction in instructions:
  action = instruction[0]
  value = instruction[1]

  if action == "N":
    y -= value
  elif action == "S":
    y += value
  elif action == "E":
    x += value
  elif action == "W":
    x -= value
  elif action == "L":
    facing = (facing - value) % 360
  elif action == "R":
    facing = (facing + value) % 360
  elif action == "F":
    if facing == 0:
      x += value
    elif facing == 90:
      y += value
    elif facing == 180:
      x -= value
    elif facing == 270:
      y -= value

print(abs(x) + abs(y))