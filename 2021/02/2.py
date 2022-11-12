import re

regex = re.compile("(\S+) (\d+)")

position = 0
depth = 0
aim = 0

with open("input") as file:
  for line in file:
    match = regex.match(line)
    instr = match.group(1)
    num = int(match.group(2))

    if instr == "forward":
      position += num
      depth += aim * num
    elif instr == "down":
      aim += num
    elif instr == "up":
      aim -= num

print(position * depth)
