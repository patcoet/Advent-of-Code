octopuses = {}

with open('input') as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line.strip()):
            octopuses[(x, y)] = int(char)

def pprint():
    width = max([x[0] for x in octopuses])
    for y in range(width + 1):
        s = ""
        for x in range(width + 1):
            o = octopuses[(x, y)]
            if o == 0:
                s += '\033[1m' + str(o) + '\033[0m'
            else:
                s += str(o)
        print(s)

pprint()

turn_counter = 1
while True:
    flashed_this_step = {}

    for octopus in octopuses:
        octopuses[octopus] += 1

    for octopus in octopuses:
        if octopuses[octopus] > 9 and octopus not in flashed_this_step:
            flashed_this_step[octopus] = True
            flashing_octopuses = [octopus]

            for f_o in flashing_octopuses:
                x, y = f_o
                for coord in [(xx, yy) for xx in range(x - 1, x + 2) for yy in range(y - 1, y + 2) if (xx, yy) in octopuses]:
                    octopuses[coord] += 1
                    if octopuses[coord] > 9 and coord not in flashed_this_step:
                        flashed_this_step[coord] = True
                        flashing_octopuses.append(coord)

    for coord in flashed_this_step:
        octopuses[coord] = 0

    print()
    pprint()
    print(turn_counter)

    if len(flashed_this_step) == len(octopuses):
        break

    turn_counter += 1
