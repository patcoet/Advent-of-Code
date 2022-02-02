lines = []

with open("input.txt") as file:
  for line in file:
    lines.append(int(line))

def get_product():
  for line1 in lines:
    for line2 in lines:
      for line3 in lines:
        if line1 != line2 and line1 != line3 and line2 != line3 and line1 + line2 + line3 == 2020:
          return line1 * line2 * line3

print(get_product())