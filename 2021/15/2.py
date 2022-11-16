from datetime import datetime


cavern = {}

with open('input') as file:
    for y, line in enumerate(file):
        for x, num in enumerate(line.strip()):
            cavern[(x, y)] = int(num)

mx, my = max(cavern)
expanded_cavern = {}

for (x, y) in cavern:
    for ix in range(5):
        for iy in range(5):
            expanded_cavern[(x+(mx+1)*ix, y+(my+1)*iy)] = (cavern[(x, y)] + ix + iy - 1) % 9 + 1

mx, my = max(expanded_cavern)

unvisited = expanded_cavern.copy()
current = (0, 0)
dists = {current: 0}

i = 0
while (mx, my) in unvisited:
    if i % 10000 == 0:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time, i)
    i += 1

    x, y = current[0], current[1]
    nbs = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for nb in nbs:
        if nb in unvisited:
            tent = dists[current] + expanded_cavern[nb]
            if nb not in dists or tent < dists[nb]:
                dists[nb] = tent

    current = min(unvisited.keys() & dists.keys(), key=lambda x: dists[x])

    del unvisited[current]

print(dists[(mx, my)])
# This gave the right answer but took 40 minutes to run, apparently mostly because of line 41. To improve some other time.
