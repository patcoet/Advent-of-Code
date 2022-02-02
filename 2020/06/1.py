groups = []

with open("input.txt") as file:
  group = ""
  for line in file:
    if line != "\n":
      group += line.strip()
    else:
      groups.append({char for char in group})
      group = ""

  groups.append({char for char in group})

print(sum(map(lambda x: len(x), groups)))