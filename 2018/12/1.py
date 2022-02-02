initial_state = ""
rules = []

with open('input.txt') as file:
  for line in file:
    if "initial" in line:
      initial_state = line[line.find('#'):].strip()
    elif line != "\n":
      words = line.strip().split(' ')
      inpt = words[0]
      outpt = words[2]
      rules.append([inpt, outpt])

# Only needed for the abbreviated example rules:
# dh = ['.', '#']
# rules = rules + [[a+b+c+d+e, '.'] for a in dh for b in dh for c in dh for d in dh for e in dh if [a+b+c+d+e, '#'] not in rules]

pots = "."*20 + initial_state + "."*20
last_generation = pots

for generation in range(20):
  for index in range(0, len(pots)):
    pot_and_neighbors = ""
    if index == 0:
      pot_and_neighbors = last_generation[0:3].rjust(5, '.')
    elif index == 1:
      pot_and_neighbors = last_generation[0:4].rjust(5, '.')
    elif index == len(last_generation)-1:
      pot_and_neighbors = last_generation[-3:].ljust(5, '.')
    elif index == len(last_generation)-2:
      pot_and_neighbors = last_generation[-4:].ljust(5, '.')
    else:
      pot_and_neighbors = last_generation[index-2:index+3]
    for rule in rules:
      inpt = rule[0]
      outpt = rule[1]
      if pot_and_neighbors == inpt:
        pots = pots[:index] + outpt + pots[index+1:]
  last_generation = pots

total = 0
for i in range(len(pots)):
  if pots[i] == '#':
    total = total + (i-20)

print(total)
