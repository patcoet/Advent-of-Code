lines = []

with open("Z:\\projects\\Advent-of-Code\\2020\\01\\input.txt") as file:
  for line in file:
    lines.append(int(line))

def get_product():
  for line1 in lines:
    for line2 in lines:
      if line1 != line2 and line1 + line2 == 2020:
        return line1 * line2

print(get_product())