inputt = 'input.txt'

polymer = ""
with open(inputt) as file:
  polymer = file.read().strip()
polymer_parts = [polymer[0:10000], polymer[10000:20000], polymer[20000:30000], polymer[30000:40000], polymer[40000:50000]]

def make_boom(letter1, letter2):
  if letter1 != letter2 and letter1.upper() == letter2.upper():
    return True
  else:
    return False

def react(polymer):
  length = len(polymer)
  index = 0
  while index < length - 1:
    letter1 = polymer[index]
    letter2 = polymer[index+1]
    if make_boom(letter1, letter2):
      polymer = polymer[0:index] + polymer[index+2:]
      length = len(polymer)
      index = index - 1
    else:
      index = index + 1
  return polymer

thing = ""
for part in polymer_parts:
  thing = thing + react(part)

print(len(react(thing)))
