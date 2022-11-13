import re

dots = {}
axis = ''
line = 0
max_x = 0
max_y = 0

with open('input') as file:
    for line in file:
        coords = re.findall('(\d+),(\d+)', line)
        instr = re.findall('fold along (\w)=(\d+)', line)
        if coords:
            x, y = int(coords[0][0]), int(coords[0][1])
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            dots[(x, y)] = True
        elif instr:
            axis, line = instr[0][0], int(instr[0][1])
            break

if axis == 'y':
    for coord in dots.copy():
        x, y = coord
        yy = max_y - y
        if y > line:
            dots[(x, yy)] = True
            del dots[(x, y)]
else:
    for coord in dots.copy():
        x, y = coord
        xx = max_x - x
        if x > line:
            dots[(xx, y)] = True
            del dots[(x, y)]

print(len(dots))
