screen = {}
w = 50
h = 6

for i in range(w):
    screen[i] = {}
    for j in range(h):
        screen[i][j] = '.'


def rect(width, height):
    for i in range(width):
        for j in range(height):
            screen[i][j] = '#'


def rotate_column(x, amount):
    tmp = {}
    for y in range(h):
        tmp[(y+amount) % h] = screen[x][y]
    screen[x] = tmp


def rotate_row(y, amount):
    tmp = {}
    for x in range(w):
        tmp[(x+amount) % w] = screen[x][y]
    for x in range(w):
        screen[x][y] = tmp[x]


def print_screen():
    for y in range(h):
        s = ""
        for x in range(w):
            s = s + screen[x][y]
        print(s)

# print_screen()


instructions = []
with open('input.txt') as file:
    for line in file:
        words = line.split()
        if words[0] == 'rect':
            wh = words[1].split('x')
            instructions.append([rect, int(wh[0]), int(wh[1])])
        elif words[0] == 'rotate':
            if words[1] == 'row':
                op = rotate_row
            elif words[1] == 'column':
                op = rotate_column

            p1 = int(words[2].split('=')[1])
            p2 = int(words[4])

            instructions.append([op, p1, p2])

for instruction in instructions:
    op = instruction[0]
    p1 = instruction[1]
    p2 = instruction[2]
    op(p1, p2)

print_screen()

counter = 0
for x in range(w):
    for y in range(h):
        if screen[x][y] == '#':
            counter = counter + 1

print(counter)
