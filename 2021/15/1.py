cavern = {}

with open('input') as file:
    for y, line in enumerate(file):
        for x, num in enumerate(line.strip()):
            cavern[(x, y)] = int(num)

mx, my = max(cavern)
unvisited = cavern.copy()
current = (0, 0)
dists = {current: 0}

while (mx, my) in unvisited:
    x, y = current[0], current[1]
    nbs = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for nb in nbs:
        if nb in unvisited:
            tent = dists[current] + cavern[nb]
            if nb not in dists or tent < dists[nb]:
                dists[nb] = tent

    del unvisited[current]

    current = min(unvisited.keys() & dists.keys(), key=lambda x: dists[x])

print(dists[(mx, my)])
