instructions = []

with open("input.txt") as file:
  for line in file:
    instructions.append([line.strip()[0], int(line.strip()[1:])])

wx = 10
wy = -1
sx = 0
sy = 0

for instruction in instructions:
  action = instruction[0]
  value = instruction[1]

  if action == "N":
    wy -= value
  elif action == "S":
    wy += value
  elif action == "E":
    wx += value
  elif action == "W":
    wx -= value
  elif action == "L":
    for n in range(value//90):
      tmp = wy
      wy = -wx
      wx = tmp
  elif action == "R":
    for n in range(value//90):
      tmp = wy
      wy = wx
      wx = -tmp
  elif action == "F":
    sx += value * wx
    sy += value * wy

print(abs(sx) + abs(sy))