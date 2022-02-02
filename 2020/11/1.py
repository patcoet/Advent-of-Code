layout = []

with open("input.txt") as file:
  for line in file:
    layout.append(line.strip())

def tick(layout):
  new_layout = []

  for y in range(len(layout)):
    new_layout.append(layout[y])

    for x in range(len(layout[y])):
      neighbors = []
      if y > 0:
        if x > 0:
          neighbors.append(layout[y-1][x-1])
        neighbors.append(layout[y-1][x])
        if x + 1 < len(layout[y]):
          neighbors.append(layout[y-1][x+1])
      if x > 0:
        neighbors.append(layout[y][x-1])
      if x + 1 < len(layout[y]):
        neighbors.append(layout[y][x+1])
      if y < len(layout) - 1:
        if x > 0:
          neighbors.append(layout[y+1][x-1])
        neighbors.append(layout[y+1][x])
        if x + 1 < len(layout[y]):
          neighbors.append(layout[y+1][x+1])

      num_occupied_neighbors = len(list(filter(lambda x: x == "#", neighbors)))

      if layout[y][x] == "L" and num_occupied_neighbors == 0:
        new_layout[y] = new_layout[y][:x] + "#" + new_layout[y][x+1:]
      elif layout[y][x] == "#" and num_occupied_neighbors >= 4:
        new_layout[y] = new_layout[y][:x] + "L" + new_layout[y][x+1:]

  return new_layout

old_layout = layout
new_layout = tick(old_layout)

while old_layout != new_layout:
  old_layout = new_layout
  new_layout = tick(new_layout)

num_occupied_seats = len(list(filter(lambda x: x == "#", "".join(new_layout))))
print(num_occupied_seats)