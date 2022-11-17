import re

xs = ()
ys = ()

with open('input') as file:
    line = file.readline()
    xs = tuple(map(int, re.findall('.*x=(-?\d+)\.\.(-?\d+)', line.strip())[0]))
    ys = tuple(map(int, re.findall('.*y=(-?\d+)\.\.(-?\d+)', line.strip())[0]))

def fire(xv, yv):
    px, py = 0, 0

    while px <= xs[1] and py >= ys[0]:
        if xs[0] <= px <= xs[1] and ys[0] <= py <= ys[1]:
            return True
        px += xv
        py += yv
        if xv > 0:
            xv -= 1
        elif xv < 0:
            xv += 1
        yv -= 1
    
    return False

min_xv = min(x for x in range(xs[0]) if x * (x + 1) / 2 >= xs[0])
max_yv = -ys[0]
valid_values = 0

for xv in range(min_xv, xs[1] + 1):
    for yv in range(ys[0], max_yv + 1):
        if fire(xv, yv):
            valid_values += 1

print(valid_values)
