heightmap = []

with open('input') as file:
    for line in file:
        heightmap.append([int(x) for x in line.strip()])

total_risk = 0
for y, row in enumerate(heightmap):
    for x, val in enumerate(row):
        nn = heightmap[y - 1][x] if y > 0 else 10
        ne = heightmap[y][x + 1] if x < len(row) - 1 else 10
        ns = heightmap[y + 1][x] if y < len(heightmap) - 1 else 10
        nw = heightmap[y][x - 1] if x > 0 else 10

        if val < nn and val < ne and val < ns and val < nw:
            total_risk += 1 + val

print(total_risk)
