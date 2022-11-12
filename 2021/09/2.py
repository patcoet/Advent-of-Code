import functools
import operator

heightmap = []

with open('input') as file:
    for line in file:
        heightmap.append([int(x) for x in line.strip()])

low_points = []
for y, row in enumerate(heightmap):
    for x, val in enumerate(row):
        nn = heightmap[y - 1][x] if y > 0 else 10
        ne = heightmap[y][x + 1] if x < len(row) - 1 else 10
        ns = heightmap[y + 1][x] if y < len(heightmap) - 1 else 10
        nw = heightmap[y][x - 1] if x > 0 else 10

        if val < nn and val < ne and val < ns and val < nw:
            low_points.append((x, y))

basins = {}
for low_point in low_points:
    x, y = low_point
    basin_points = [(x, y)]

    for point in basin_points:
        px, py = point
        nn = heightmap[py - 1][px] if py > 0 else None
        ne = heightmap[py][px + 1] if px < len(heightmap[py]) - 1 else None
        ns = heightmap[py + 1][px] if py < len(heightmap) - 1 else None
        nw = heightmap[py][px - 1] if px > 0 else None

        nnp = (px, py - 1)
        nep = (px + 1, py)
        nsp = (px, py + 1)
        nwp = (px - 1, py)

        for (nx, nxp) in [(nn, nnp), (ne, nep), (ns, nsp), (nw, nwp)]:
            if nx and nx < 9 and nxp not in basin_points:
                basin_points.append(nxp)

    basins[low_point] = basin_points

print(functools.reduce(operator.mul, sorted([len(x) for x in basins.values()])[-3:]))
