lines = []

with open("input.txt") as file:
  for line in file:
    lines.append(line.strip())

def traverse(x_step, y_step):
  x = 0
  y = 0
  tree_counter = 0

  while y < len(lines):
    if lines[y][x] == "#":
      tree_counter += 1

    x = (x + x_step) % len(lines[y])
    y += y_step

  return tree_counter

print(traverse(1, 1) * traverse(3, 1) * traverse(5, 1) * traverse(7, 1) * traverse(1, 2))