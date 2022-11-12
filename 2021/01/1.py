increases = 0

with open("input") as file:
  last_line = -1
  for line in file:
    if last_line > 0 and int(line) > last_line:
      increases += 1
    last_line = int(line)

print(increases)
