import string

groups = []

with open("input.txt") as file:
  group = []
  for line in file:
    if line != "\n":
      group.append(line.strip())
    else:
      groups.append(group)
      group = []

  groups.append(group)

sum_ = 0

for group in groups:
  for char in string.ascii_lowercase[:27]:
    if all(map(lambda x: char in x, group)):
      sum_ += 1

print(sum_)