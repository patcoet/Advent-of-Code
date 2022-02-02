lines = []

with open("input.txt") as file:
  for line in file:
    if line.find("shiny gold bags contain") == -1:
      lines.append(line.strip())

wanted = {"shiny gold"}
wanted2 = set()

while True:
  for line in lines:
    for bag_type in wanted:
      if line.find(bag_type) != -1:
        wanted2.add(' '.join(line.split()[:2]))

  if wanted.difference({"shiny gold"}) == wanted2:
    break

  wanted = wanted.union(wanted2)

print(len(wanted2))