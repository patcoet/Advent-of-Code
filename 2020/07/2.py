import regex

lines = []

with open("input.txt") as file:
  for line in file:
    line = line.strip().split()
    color = ' '.join(line[:2])
    contents = []
    for item in ' '.join(line[4:]).split(","):
      list_ = item.strip().strip(".").split()[:-1]
      if len(list_) > 2:
        number = int(list_[0])
        contents.append([number, ' '.join(list_[1:])])
    lines.append([color, contents])

def weight(name):
  for line in lines:
    if line[0] == name:
      node = line

  if node[1] == []:
    return 1

  sum_ = 0

  for sub in node[1]:
    sum_ += sub[0] * weight(sub[1])

  return sum_ + 1

print(weight('shiny gold') - 1)
