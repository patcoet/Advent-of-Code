import re

xs = ()
ys = ()

with open('input') as file:
    line = file.readline()
    xs = tuple(map(int, re.findall('.*x=(-?\d+)\.\.(-?\d+)', line.strip())[0]))
    ys = tuple(map(int, re.findall('.*y=(-?\d+)\.\.(-?\d+)', line.strip())[0]))

def fire(px, py, xv, yv):
    highest = py
    hit = False
    last_py = py
    going_up = True
    while px <= xs[1] and py >= ys[0]:
        if going_up and py < last_py:
            going_up = False
        if going_up:
            highest = max(highest, py)
        if xs[0] <= px <= xs[1] and ys[0] <= py <= ys[1]:
            hit = True
            break
        px += xv
        py += yv
        if xv > 0:
            xv -= 1
        elif xv < 0:
            xv += 1
        yv -= 1
    
    return hit and highest

highest = 0
min_xv = min(x for x in range(xs[0]) if x * (x + 1) / 2 >= xs[0])
max_yv = -ys[0]
for x in range(min_xv, xs[1]):
    for y in range(max_yv + 1):
        highest = max(highest, fire(0, 0, x, y))

print(highest)
