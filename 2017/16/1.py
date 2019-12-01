inputt = 'input.txt'

dance_steps = []
with open(inputt) as file:
  dance_steps = file.read().strip().split(',')

line = [chr(x) for x in range(ord('a'), ord('p')+1)]

for step in dance_steps:
  print(step.ljust(10), ''.join(line))
  instruction = step[0]
  if instruction == 's':
    num = int(step[1:])
    line = line[-num:] + line[:-num]
  if instruction == 'x':
    a = int(step[1:].split('/')[0])
    b = int(step[1:].split('/')[1])
    tmp = line[a]
    line[a] = line[b]
    line[b] = tmp
  if instruction == 'p':
    a = step[1:].split('/')[0]
    b = step[1:].split('/')[1]
    line = list(map(lambda s: s.replace(a, 'x').replace(b, a).replace('x', b), line))

print(''.ljust(10), ''.join(line))
