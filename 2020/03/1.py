lines = []

with open("input.txt") as file:
    for line in file:
        lines.append(line.strip())

tree_counter = 0
x = 0

for line in lines:
    if line[x] == "#":
        tree_counter += 1

    x = (x + 3) % len(line)

print(tree_counter)
