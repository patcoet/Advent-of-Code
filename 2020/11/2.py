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
      if layout[y][x] != ".":
        for k in range(1, min(x, y) + 1):
          if y-k >= 0 and x-k >= 0 and layout[y-k][x-k] != ".":
            neighbors.append(layout[y-k][x-k])
            break

        for k in range(1, y+1):
          if y-k >= 0 and layout[y-k][x] != ".":
            neighbors.append(layout[y-k][x])
            break

        for k in range(1, min(len(layout[y])-x-1, y) + 1):
          if y-k >= 0 and x+k < len(layout[y]) and layout[y-k][x+k] != ".":
            neighbors.append(layout[y-k][x+k])
            break

        for k in range(1, x+1):
          if x-k >= 0 and layout[y][x-k] != ".":
            neighbors.append(layout[y][x-k])
            break

        for k in range(1, len(layout[y])-x):
          if x+k < len(layout[y]) and layout[y][x+k] != ".":
            neighbors.append(layout[y][x+k])
            break

        for k in range(1, min(len(layout)-y-1, x) + 1):
          if y+k < len(layout) and x-k >= 0 and layout[y+k][x-k] != ".":
            neighbors.append(layout[y+k][x-k])
            break

        for k in range(1, len(layout)-y):
          if y+k < len(layout) and layout[y+k][x] != ".":
            neighbors.append(layout[y+k][x])
            break

        for k in range(1, min(len(layout)-y, len(layout[y])-x)):
          if y+k < len(layout) and x+k < len(layout[y]) and layout[y+k][x+k] != ".":
            neighbors.append(layout[y+k][x+k])
            break

      num_occupied_neighbors = len(list(filter(lambda x: x == "#", neighbors)))

      if layout[y][x] == "L" and num_occupied_neighbors == 0:
        new_layout[y] = new_layout[y][:x] + "#" + new_layout[y][x+1:]
      elif layout[y][x] == "#" and num_occupied_neighbors >= 5:
        new_layout[y] = new_layout[y][:x] + "L" + new_layout[y][x+1:]

  return new_layout

old_layout = layout
new_layout = tick(old_layout)

while old_layout != new_layout:
  old_layout = new_layout
  new_layout = tick(new_layout)

num_occupied_seats = len(list(filter(lambda x: x == "#", "".join(new_layout))))
print(num_occupied_seats)