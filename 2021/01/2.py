increases = 0

with open("input") as file:
  last_three = [0, 0, 0]
  for line in file:
    if 0 not in last_three and sum(last_three[1:]) + int(line) > sum(last_three):
      increases += 1
    last_three.append(int(line))
    last_three.pop(0)

print(increases)
