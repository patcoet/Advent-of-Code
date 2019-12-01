class Component:
  def __init__(self, i, o, value, length=1):
    self.i = i
    self.o = o
    self.value = value
    self.length = length

  def combine(self, other):
    if self.o == other.i:
      return Component(self.i, other.o, self.value + other.value, self.length + other.length)
    elif self.o == other.o:
      return Component(self.i, other.i, self.value + other.value, self.length + other.length)
    else:
      return None

def read(filename):
  components = []

  with open(filename) as file:
    for line in file:
      io = line.strip().split('/')
      components.append(Component(io[0], io[1], int(io[0]) + int(io[1])))

  return components

def recurse(prev_match, cs, cc):
  cs = [c for c in cs if c != cc]
  for cc in cs:
    match = prev_match.combine(cc)
    if match:
      matches.append(match)
      recurse(match, cs, cc)

components = read('input.txt')
component0 = Component('0', '0', 0)
matches = []

recurse(component0, components, None)

matches.sort(key=lambda x: x.value, reverse=True)
matches.sort(key=lambda x: x.length, reverse=True)
print(matches[0].value)
